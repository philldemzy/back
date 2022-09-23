from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("exam/setup", views.set_test, name="set_exam"),
    path("exam/setup/<str:task_id>", views.set_test_progress, name="set_exam_progress"),
    path("take/<str:link>", views.get_test, name="get_exam"),
    path("mark", views.mark_test, name="mark_exam"),
    path("mark/<str:task_id>", views.mark_test_progress, name="mark_test_progress"),
    path("check/<str:link>", views.check_test, name="check_exam"),
    path("prev/<str:link>", views.preview_and_edit_test, name="preview_and_edit_test"),
]
