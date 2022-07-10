from django.db import models

# Create your models here.
"""
Create table for setting test, Table would have unique link that will start capital letters.
pk, link(Examiner's), URL to Text file containing questions and answers
Create table for taking test, Table would have uniques link starting with small letters.
pk, link(Students), students name
Table for exams statistics
"""


class Exam(models.Model):
    exam_name = models.CharField(max_length=70)
    examiner_link = models.CharField(max_length=25, unique=True)
    test_link = models.CharField(max_length=25, unique=True)
    test_instructions = models.CharField(max_length=100)
    test_file = models.FileField(upload_to='posts/%Y/%m/%d')
    start_time = models.DateTimeField(null=True, blank=True)
    total_score = models.IntegerField()
    duration = models.DurationField()

    def __str__(self):
        return f'{self.exam_name} starting on {self.start_time.day}'


class TestTaker(models.Model):
    test = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name="get_exam")
    student_id = models.CharField(max_length=100)
    student_name = models.CharField(max_length=150)
    score = models.IntegerField(null=True, blank=True)


class Question(models.Model):
    test = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name="exam_of_qns")
    question = models.CharField(max_length=400)
    answer = models.CharField(max_length=100)


class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="option_question")
    option = models.CharField(max_length=100)
