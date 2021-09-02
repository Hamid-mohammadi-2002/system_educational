from django.contrib import admin

# Register your models here.
from university.models import College, Classes, Professor, Lesson, Student
from library.models import Book

@admin.action(description='Mark selected class as closed')
def make_closed(modeladmin, request, queryset):
    queryset.update(status=False)


@admin.action(description='Mark selected class as opened')
def make_opened(modeladmin, request, queryset):
    queryset.update(status=True)


@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    pass


@admin.register(Classes)
class ClassesAdmin(admin.ModelAdmin):
    actions = [make_closed, make_opened]


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    pass


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    pass


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(Book)
class StudentAdmin(admin.ModelAdmin):
    pass
