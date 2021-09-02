from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Classes, Student
from django.views.generic import ListView
from .forms import StudentForm


class ClassesListView(ListView):
    context_object_name = 'Classes'
    queryset = Classes.objects.filter(status=True)
    template_name = 'university/index.html'


def get_lessons_and_students(request, class_id):
    context = dict()
    students_list = Classes.objects.get(pk=class_id)
    context['students_list'] = students_list
    print(students_list)
    return render(request, 'university/students_list.html', context)


@login_required
def register_student(request):
    context = dict()

    if request.method == 'GET':
        form = StudentForm(initial={'first_name': request.user, 'last_name': request.user.last_name})
        context['form'] = form
        return render(request, 'university/register_student.html', context)

    form = StudentForm(request.POST)
    if form.is_valid():
        student_first_name = form.cleaned_data['first_name']
        student_last_name = form.cleaned_data['last_name']
        lessons = form.cleaned_data['lesson']
        grade = form.cleaned_data['grade']
        print(form.cleaned_data)

        new_student = Student.objects.create(first_name=student_first_name, last_name=student_last_name,
                                             grade=grade)
        new_student.lesson.set(lessons)
        new_student.save()
        print(new_student)
        messages.success(request, 'You are successfully registered.')
        return redirect('university:index')
