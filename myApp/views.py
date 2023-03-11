from json import loads as json_loads
from pickle import loads as pickle_loads, dumps as pickle_dumps
from datetime import timedelta, datetime
from os import environ

from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.http import HttpRequest

import logging

from celery.result import AsyncResult

from .serializer import send_question, send_exam_info, send_preview_question
from .models import Exam, TestTaker, Question, Option
from .helpers.utils import generate_examiner_link, generate_exam_link, get_datetime_obj, get_duration
from .tasks import process_file, mark_tests


# Get an instance of a logger
logger = logging.getLogger(__name__)


# my auth style
@csrf_exempt
def auth(request):
    if request.method == "POST":
        key = request.POST.get('authKey')
        if key == environ["AUTHKEY"]:
            return redirect('candy')
        return JsonResponse({'!!': '!!'}, status=404)
    return JsonResponse({'error': 'wrong request method'}, status=404)


@ensure_csrf_cookie
def index(request):
    logger.info(f'\n')
    logger.info(f'::::::: token req :::::::')
    res = JsonResponse({'token': get_token(request)})
    logger.info(f'::::::: token sent :::::::')
    return res


# Create a new exam
def set_test(request):
    logger.info(f'\n')
    logger.info(f'::::::: set test req :::::::')
    if request.method == "POST":
        logger.info(f'request ==> {request.POST}')
        try:
            # Get duration of exam
            hours = request.POST.get('hours')  # Get hours of exam duration
            minutes = request.POST.get('minutes')  # Get minutes of exam duration

            # Convert string of time to datetime object (%d:%m:%y:%H:%M e.g '28:09:22:20:43')
            time = request.POST.get('time').split(':')
            start_time = get_datetime_obj(time)  # Convert to datetime object

            file = request.FILES.get('exam')
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
                total_score=0
            )
            new_exam.save()

            res = process_file.delay(new_exam.test_file.path, new_exam.id)  # Processing of file done async
            logger.info(f'::::::: request sent to celery successfully :::::::')
            return JsonResponse({
                'examiner_link': new_exam.examiner_link,
                'test_link': new_exam.test_link,
                'task': res.id
            }, status=202)

        except Exception as err:
            logger.error(f'an error occurred: {err}')
            logger.info(f'::::::: request not sent to celery successfully :::::::')
            return JsonResponse({'error': 'An input detail is left out'}, status=400)

    logger.info(f'::::::: wrong request method :::::::')
    return JsonResponse({'bad': 'wrong method'}, status=404)


# View for checking result of celery async task and progress information
def set_test_progress(request, task_id):
    """
    Reporting task result to front end which would ping back till task is done
    """
    logger.info(f'\n')
    logger.info(f'::::::: set test progress req :::::::')
    logger.info(f'{task_id}')
    try:
        task = AsyncResult(task_id)
    except Exception as err:
        logger.error(f'an error occurred: {err}')
        logger.warning(f'::::::: request end :::::::')
        return JsonResponse({"error": "task not found"}, status=400)

    # Checking if task has started or is still pending
    if task.state == 'FAILURE' or task.state == 'PENDING':
        response = {
            'task_id': task_id,
            'state': task.state,
            'info': str(task.info)
        }
        logger.warning(f"task({task_id}) state is {task.state}")
        logger.warning(f'::::::: request end :::::::')
        return JsonResponse(response, status=200)

    # Get result value
    info = True if task.get() == 'success' else task.get().get('error')
    response = {
        'task_id': task_id,
        'state': task.state,
        'info': info
    }
    if info:
        logger.info(f"test questions processed successfully")
    else:
        logger.warning(f"task state is {task.state}")
    logger.info(f'::::::: request end :::::::')
    return JsonResponse(response, status=200)


# View for getting questions for exam and registration
def get_test(request, link):
    # Getting exam info
    logger.info(f'\n')
    logger.info(f'::::::: get test req :::::::')
    logger.info(f"test_link: {link}")
    if f'exam_{link}' in request.session:  # Check if exam is in session
        exam = pickle_loads(request.session[f'exam_{link}'])  # Using pickle to get query object from session
    else:  # User just starting exam
        try:
            exam = Exam.objects.get(test_link=link)
            request.session[f'exam_{link}'] = pickle_dumps(exam)  # Using pickle to store the query object in session
            request.session.set_expiry(exam.duration.total_seconds())
        except Exception as err:
            logger.error(f'an error occurred: {err}')
            logger.warning(f'::::::: request end :::::::')
            return JsonResponse({'error': 'Exam with link does not exist'}, status=404)

    if request.method == "POST":
        try:
            student_id = request.POST["student_id"]
            student_name = request.POST["student_name"]
        except Exception as err:
            logger.error(f'an error occurred: {err}')
            logger.warning(f'::::::: request end :::::::')
            return JsonResponse({'error': 'An input detail is left out'}, status=400)

        # Checking if user has registered for that exam
        registered = TestTaker.objects.filter(test=exam, student_id=student_id).first()
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
        if datetime.now(tz=exam.start_time.tzinfo) >= exam.start_time:
            # Send questions to client side only if exam has not ended
            if datetime.now(tz=exam.start_time.tzinfo) <= exam.start_time + exam.duration:
                questions = Question.objects.prefetch_related('option_question').filter(test=exam)
                # use Json format
                logger.info(f'::::::: request ended (test returned) :::::::')
                return JsonResponse({
                    'name': exam.exam_name,
                    'start_time': exam.start_time.isoformat(),
                    'duration': exam.duration.total_seconds(),
                    'mark': exam.total_score,
                    'student': registered.id,
                    'questions': [send_question(question) for question in questions],
                }, safe=False)

            # Exam has ended
            logger.info(f'::::::: request ended (test ended) :::::::')
            return JsonResponse({'expired': 'Exam has ended'}, status=403)

        # If exam has not started
        logger.info(f'::::::: request ended (test not started) :::::::')
        return JsonResponse({'not_time': 'Test has not started'}, status=403)

    # Get method
    logger.info(f'::::::: request ended (test details returned) :::::::')
    return JsonResponse({
        'name': exam.exam_name,
        'start_time': exam.start_time.isoformat(),
        'duration': get_duration(exam.duration.total_seconds()),
        'mark': exam.total_score,
        'instructions': exam.test_instructions,
        'ended': datetime.now(exam.start_time.tzinfo) > exam.start_time + exam.duration
        if datetime.now(exam.start_time.tzinfo) > exam.start_time + exam.duration else exam.start_time.isoformat(),
    }, status=200, safe=False)


# View for submitting answers
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
    logger.info(f'\n')
    logger.info(f'::::::: mark test req :::::::')
    if request.method == "POST":
        # Get info from client side
        data = json_loads(request.body)
        logger.info(f"request ==> {data}")
        student = TestTaker.objects.get(pk=data.get('student')['pk'])
        student.answers = data
        student.save()  # save data to be processed incase or disaster
        res = mark_tests.delay(data)

        # return success
        logger.info(f'::::::: request sent to celery successfully :::::::')
        return JsonResponse({'task': res.id}, status=202)

    logger.info(f'::::::: wrong request method :::::::')
    return JsonResponse({'bad': 'wrong method'}, status=404)


def mark_test_progress(request, task_id):
    """
    Reporting task result to front end which would ping back till task is done
    """
    logger.info(f'\n')
    logger.info(f':::::::  mark test progress req :::::::')
    logger.info(f'{task_id}')
    try:
        task = AsyncResult(task_id)
    except Exception as err:
        logger.error(f'an error occurred: {err}')
        logger.warning(f'::::::: request end :::::::')
        return JsonResponse({"error": "task not found"}, status=400)

    # Checking if task has started or is still pending
    if task.state == 'FAILURE' or task.state == 'PENDING':
        response = {
            'task_id': task_id,
            'state': task.state,
            'info': str(task.info)
        }
        logger.warning(f"task({task_id}) state is {task.state}")
        logger.warning(f'::::::: request end :::::::')
        return JsonResponse(response, status=200)

    response = {
        'task_id': task_id,
        'state': task.state,
        'info': "None"
    }
    if task.state == 'success':
        logger.info(f"test questions processed successfully")
    else:
        logger.warning(f"task state is {task.state}")
    logger.info(f'::::::: request end :::::::')
    return JsonResponse(response, status=200)


# View for checking statistics of an exam
def check_test(request, link):
    """
    Send all database related info about an exam to client
    Front end will deal with analysing data
    """
    logger.info(f'\n')
    logger.info(f'::::::: check test req :::::::')
    logger.info(f"test_link: {link}")
    try:
        exam = Exam.objects.prefetch_related('get_exam').get(examiner_link=link)
    except Exception as err:
        logger.error(f'an error occurred: {err}')
        logger.warning(f'::::::: request end :::::::')
        return JsonResponse({'error': 'exam does not exist'}, status=400)

    # add checks for if results have been collated
    if datetime.now(tz=exam.start_time.tzinfo) >= exam.start_time + exam.duration:
        logger.info(f'::::::: request ended (test returned) :::::::')
        return JsonResponse(send_exam_info(exam))  # send student scores and info about an exam

    elif datetime.now(tz=exam.start_time.tzinfo) <= exam.start_time:
        logger.info(f'::::::: request ended (test not started) :::::::')
        return JsonResponse({
            'completed': False,
            'title': exam.exam_name,
            'total_score': exam.total_score,
            'start_time': exam.start_time.isoformat(),
            'duration': get_duration(exam.duration.total_seconds()),
        })

    logger.info(f'::::::: request ended (test ongoing) :::::::')
    return JsonResponse({
        'completed': False,
        'title': exam.exam_name,
        'total_score': exam.total_score,
        'start_time': exam.start_time.isoformat(),
        'duration': get_duration(exam.duration.total_seconds()),
    })


# View for previewing and editing exam
def preview_and_edit_test(request, link):
    logger.info(f'\n')
    logger.info(f'::::::: prev/edit test req :::::::')
    logger.info(f"test_link: {link}")

    try:
        exam = Exam.objects.get(examiner_link=link)
        questions = Question.objects.prefetch_related('option_question').filter(test=exam)
    except Exception as err:
        logger.error(f'an error occurred: {err}')
        logger.warning(f'::::::: request end :::::::')
        return JsonResponse({'error': 'Exam with link does not exist'}, status=404)

    if request.method == "PUT":
        # Only edit questions if exam has not started
        if datetime.now(tz=exam.start_time.tzinfo) <= exam.start_time:
            data = json_loads(request.body)
            logger.info(f'request ==> {data}')

            if data.get('type') == 'question':
                quest = Question.objects.get(pk=data.get('id'))
                quest.question = data.get('data')
                quest.save()

                logger.info(f'::::::: question successfully changed :::::::')
                return JsonResponse({'type': 'question', 'id': quest.id, 'data': quest.question})

            elif data.get('type') == 'option':
                opt = Option.objects.get(pk=data.get('id'))
                opt.option = data.get('data')
                opt.save()

                logger.info(f'::::::: option successfully changed :::::::')
                return JsonResponse({'type': 'option', 'id': opt.id, 'data': opt.option})

            elif data.get('type') == 'answer':
                quest = Question.objects.get(pk=data.get('id'))
                quest.answer = data.get('data')
                quest.save()

                logger.info(f'::::::: answer successfully changed :::::::')
                return JsonResponse({'type': 'answer', 'id': quest.id, 'data': quest.answer})

        # Return error
        logger.error(f'::::::: test ended or ongoing :::::::')
        return JsonResponse({'error': 'exam in progress or has ended'}, status=403)

    logger.info(f'::::::: test details sent :::::::')
    return JsonResponse({
        'name': exam.exam_name,
        'start_time': exam.start_time.isoformat(),
        'duration': get_duration(exam.duration.total_seconds()),
        'mark': exam.total_score,
        'questions': [send_preview_question(question) for question in questions],
    }, safe=False)
