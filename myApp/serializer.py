"""Serializers"""


def send_question(question):
    return {
        'id': question.id,
        'question': question.question,
        'options': [qes.option for qes in question.option_question.all()]
    }


def send_exam_info(exam):
    return {
        'title': exam.exam_name,
        'total_score': exam.total_score,
        'start_time': exam.start_time,
        'duration': exam.duration,
        'students': [{'student_id': student.student_id, 'student_name': student.student_name, 'score': student.score}
                     for student in exam.get_exam.all()]
    }
