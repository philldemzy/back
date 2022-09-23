from re import compile

from celery import shared_task

from .models import Question, TestTaker, Exam, Option


# Processing file function
@shared_task(bind=True)
def process_file(self, file_location, exam_id):
    """
       We are having one format for now
       {
       N. Q
       0. O(max of 4, separated by ' ')
       answer= A
       }
       where N is number of question
       where o is option identifier (max of 5)
       where answer= is answer identifier
       where Q is question
       where O is option
       where A is the answer
       """
    try:
        exam = Exam.objects.get(pk=exam_id)
        with open(file_location) as f:
            my_file = f.read()
            q = compile('[%][\\d]+')
            o = compile('[%][a-z]')
            ans = compile('answer=')
            questions = q.split(my_file)  # Split file into used format
            total_q = len(questions)
            if total_q > 50:  # Questions must not be more than 50
                return False
            i = 0
            while i < total_q:
                options = o.split(questions[i])  # Getting all options and question
                total_options = len(options)
                if total_options < 2:  # Incase lines dont have options
                    i += 1
                    continue
                qtn = options.pop(0).strip()  # Get Exact question
                total_options = len(options)
                answer = ans.split(options[total_options - 1])[1].strip()  # Get Answer
                options[total_options - 1] = ans.split(options[total_options - 1])[0].strip()  # Remove answer
                new_qtn = Question(
                    test=exam,
                    question=qtn,
                    answer=answer
                )
                new_qtn.save()  # add question to question table
                tot_len = len(options)
                total_options = tot_len if tot_len < 4 else 4
                j = 0
                while j < total_options:
                    new_option = Option(
                        question=new_qtn,
                        option=options[j].strip()
                    )
                    new_option.save()  # add options to option table
                    j += 1
                i += 1
                self.update_state(state='PROGRESS', meta={'current': i, 'total': total_q})
        return True
    except IOError:
        return {'Error': 'File Can Not Be Opened'}
    except Exception as err:
        return {'Error': f"Unexpected error is {repr(err)}"}


# Marking test function
@shared_task(bind=True)
def mark_tests(self, data):
    # Counter for total score
    total_score = 0

    # Loop through answers to get question and check answers
    i = 0
    while i < len(data.get("answers")):
        choice = data.get("answers")[i].get("answer")
        question = Question.objects.get(pk=data.get("answers")[i].get("id"))
        # Get if answer equals choice
        if question.answer == choice:
            total_score += 1
        i += 1
        self.update_state(state='PROGRESS', meta={'current': i, 'total': len(data.get("answers"))})

    # After marking update score of test taker in the table
    test_taker = TestTaker.objects.get(student_id=data.get("student")["student_id"],
                                          test=Exam.objects.get(test_link=data.get("student")["test_link"]))
    test_taker.score = total_score
    test_taker.save()
    return True
