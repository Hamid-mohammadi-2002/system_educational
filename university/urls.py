from django.urls import path
from .views import ClassesListView, get_lessons_and_students, register_student

app_name = 'university'

urlpatterns = [
    path('', ClassesListView.as_view(), name='index'),
    path('student_list/<int:class_id>/', get_lessons_and_students, name='students_list'),
    path('register_students/', register_student, name='registere_students'),
]
