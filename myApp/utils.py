from re import compile
from datetime import datetime
from random import choice

from django.utils.crypto import get_random_string

from .models import Exam, Question, Option


# generate examiner link of len ten
def generate_examiner_link():
    string_ = choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    string_ += get_random_string(9)
    if Exam.objects.filter(examiner_link=string_).first() is None:
        return string_
    generate_examiner_link()


# generate exam link of len ten
def generate_exam_link():
    string_ = choice('abcdefghijklmnopqrstuvwxyz')
    string_ += get_random_string(9)
    if Exam.objects.filter(test_link=string_).first() is None:
        return string_
    generate_exam_link()


# Convert time gotten from client side to datetime object
def get_datetime_obj(time):
    time_format = f'{time[0]}/{time[1]}/{time[2]} {time[3]}:{time[4]}:{0} +0000'
    start_time = datetime.strptime(time_format, '%d/%m/%y %H:%M:%S %z')
    return start_time


# reading and analysing file
def read_file(file_location, exam_id):
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
            q = compile('[\\d]+[.]')
            o = compile('[a-e][.]')
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
        return True
    except IOError:
        return {'Error': 'File Can Not Be Opened'}
    except Exception as err:
        return {'Error': f"Unexpected error is {repr(err)}"}
