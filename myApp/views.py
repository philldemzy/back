from json import loads as json_loads
from pickle import loads as pickle_loads, dumps as pickle_dumps
from datetime import timedelta, datetime

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from celery.result import AsyncResult

from .serializer import send_question, send_exam_info
from .models import Exam, TestTaker, Question
from .utils import generate_examiner_link, generate_exam_link, get_datetime_obj, get_duration
from .tasks import process_file, mark_tests


# Create your views here.
def index(request):
    if request.method == "POST":
        return HttpResponse('Think of a project')  # This is nonsense btw
    return render(request, "myApp/index.html")


# Create a new exam
@csrf_exempt
def set_test(request):
    if request.method == "POST":
        # Get duration of exam
        hours = request.POST.get('hours')  # Get hours of exam duration
        minutes = request.POST.get('minutes')  # Get minutes of exam duration

        # Convert string of time to datetime object (%d:%m:%y:%H:%M e.g '23:04:22:06:20')
        time = request.POST.get('time').split(':')
        start_time = get_datetime_obj(time)  # Convert to datetime object

        file = request.FILES.get('exam')
        score = request.POST.get('final_score')
        exam_name = request.POST.get('test_name')
        test_instructions = request.POST.get('test_instructions')

        new_exam = Exam(
            exam_name=exam_name,
            examiner_link=generate_examiner_link(),
            test_link=generate_exam_link(),
            test_file=file,
            test_instructions=test_instructions,
            start_time=start_time,
            duration=timedelta(hours=int(hours), minutes=int(minutes)),
            total_score=score
        )
        new_exam.save()

        res = process_file.delay(new_exam.test_file.path, new_exam.id)  # Processing of file done async
        return JsonResponse({'task': res.id}, status=202)


# View for checking result of celery async task and progress information
def set_test_progress(request, task_id):
    """
    Reporting task result to front end which would ping back till task is done
    """
    task = AsyncResult(task_id)

    # Checking if task has started or is still pending
    if task.state == 'FAILURE' or task.state == 'PENDING':
        response = {
            'task_id': task_id,
            'state': task.state,
            'info': str(task.info)
        }
        return JsonResponse(response, status=200)

    current = task.info.get('current', 0)
    total = task.info.get('total', 1)
    progression = (int(current) / int(total)) * 100  # to display a percentage of progress of the task
    response = {
        'task_id': task_id,
        'state': task.state,
        'progression': progression,
        'info': "None"
    }
    return JsonResponse(response, status=200)


def expln(request):
    return render(request, "myApp/expln.html")


def newtst(request):
    return render(request, "myApp/new_test.html")


# View for getting questions for exam and registration
@csrf_exempt
def get_test(request, link):
    # Getting exam info
    if f'exam_{link}' in request.session:  # Check if exam is in session
        exam = pickle_loads(request.session['exam'])  # Using pickle to get query object from session
    else:  # User just starting exam
        exam = Exam.objects.get(test_link=link)
        request.session['exam'] = pickle_dumps(exam)  # Using pickle to store the query object in session
        request.session.set_expiry(exam.duration.total_seconds())

    if request.method == "POST":
        student_id = request.POST["student_id"]
        student_name = request.POST["student_name"]

        # Checking if user has registered for that exam
        registered = TestTaker.objects.filter(test=exam, student_id=student_id, student_name=student_name).first()
        # Register user if not registered
        if not registered:
            registered = TestTaker(
                test=exam,
                student_id=student_id,
                student_name=student_name
            )
            registered.save()
        """
        If user has started exam and mistakenly exited time wont be added unfortunately
        But user session would be stored from client side for answers user has already answered
        TODO Probably as user answers the answer would be sent directly to server
        For now answers would be kept in the client side till user clicks submit
        """
        # Check if exam has started
        if datetime.now(exam.start_time.tzinfo) >= exam.start_time:
            # Send questions to client side only if exam has not ended
            if datetime.now(exam.start_time.tzinfo) <= exam.start_time + exam.duration:
                questions = Question.objects.prefetch_related('option_question').filter(test=exam)
                # use Json format
                return JsonResponse({
                    'name': exam.exam_name,
                    'start_time': exam.start_time,
                    'duration': exam.duration,
                    'mark': exam.total_score,
                    'student': registered.id,
                    'questions': [send_question(question) for question in questions]
                }, safe=False)
                
            # Exam has ended
            return JsonResponse({'Expired': 'Exam has ended'}, status=403)

        # If exam has not started
        return JsonResponse({'Not time': 'Test has not started'}, status=403)

    # Get method
    return JsonResponse({
        'name': exam.exam_name,
        'start_time': exam.start_time,
        'duration': get_duration(exam.duration.total_seconds()),
        'mark': exam.total_score,
        'instructions': exam.test_instructions,
        'ended': datetime.now(exam.start_time.tzinfo) > (exam.start_time + exam.duration)
        if datetime.now(exam.start_time.tzinfo) > (exam.start_time + exam.duration) else exam.start_time.isoformat(),
    }, status=200, safe=False)


# View for submitting answers
@csrf_exempt
def mark_test(request):
    """
    After each test taker submits their tests it gets marked in this route
    A messaging queue would be used for this route
    Client side should just get id of questions and answers picked for each question
    {
    student: student.id,
    answers: [{id: question.id,
            answer: question.answer}, ...]
    }
    """
    if request.method == "POST":
        # Get info from client side
        data = json_loads(request.body)
        res = mark_tests.delay(data)

        # return success
        return JsonResponse({'task': res.id}, status=202)
    return JsonResponse({'Error': 'Only post allowed'}, status=403)


def mark_test_progress(request, task_id):
    """
    Reporting task result to front end which would ping back till task is done
    """
    task = AsyncResult(task_id)

    # Checking if task has started or is still pending
    if task.state == 'FAILURE' or task.state == 'PENDING':
        response = {
            'task_id': task_id,
            'state': task.state,
            'info': str(task.info)
        }
        return JsonResponse(response, status=200)

    current = task.info.get('current', 0)
    total = task.info.get('total', 1)
    progression = (int(current) / int(total)) * 100  # to display a percentage of progress of the task
    response = {
        'task_id': task_id,
        'state': task.state,
        'progression': progression,
        'info': "None"
    }
    return JsonResponse(response, status=200)


# View for checking statistics of an exam
def check_test(request, link):
    """
    Send all database related info about an exam to client
    Front end will deal with analysing data
    """
    exam = Exam.objects.prefetch_related('get_exam').get(examiner_link=link)

    # add checks for if results have been collated
    if datetime.now(exam.start_time.tzinfo) >= exam.start_time + exam.duration:
        return JsonResponse(send_exam_info(exam))  # send student scores and info about an exam

    elif datetime.now(exam.start_time.tzinfo) <= exam.start_time:
        return JsonResponse({'Not yet': 'Exam not started'})

    return JsonResponse({'Not yet': 'Exam in progress'})
