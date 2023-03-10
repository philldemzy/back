from django.contrib import admin

from .models import Exam, TestTaker, Question, Option

# Register your models here.
admin.site.register(Exam)
admin.site.register(TestTaker)
admin.site.register(Question)
admin.site.register(Option)
