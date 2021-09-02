from django.contrib.auth import get_user_model
from django.db import models

CustomUser = get_user_model()


class University(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'university'
        verbose_name_plural = 'University'
        db_table = 'university'


class College(models.Model):
    college_name = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.college_name}'

    class Meta:
        verbose_name = 'College'
        verbose_name_plural = 'Colleges'
        db_table = 'Colleges'


class Employee(CustomUser):
    college_name = models.ForeignKey(College, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name}{self.user.last_name}'

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        db_table = 'Employees'
        permissions = [
                ('can_edit_lessons', 'Can edit students lessons ' ),
                ('can_edit_info', 'Can edit students info ' ),
        ]


class Major(models.Model):
    name = models.CharField(max_length=150)
    college_name = models.ForeignKey(College, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name}{self.user.last_name}'

    class Meta:
        verbose_name = 'Major'
        verbose_name_plural = 'Majors' 
        db_table = 'Mjaors'


class Professor(CustomUser):
    field = models.ForeignKey(Major, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name}{self.user.last_name}'

    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professors'
        permissions = [
                ('can_edit_lessons', 'Can edit students lessons ' ),
        ]
        db_table = 'Professors'


class Lesson(models.Model):
    name = models.CharField(max_length=150)
    major = models.ForeignKey(Major, on_delete=models.CASCADE)
    unit = models.SmallIntegerField(default=1)
    professor_name = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'
        db_table = 'Lessons'


class Student(CustomUser):
    BACHELOR = 'BACHELOR'
    MASTER = 'MASTER'
    PhD = 'PhD'
    POSTDOC = 'POSTDOC'

    GRADES_CHOICES = [
        (BACHELOR, 'Bachelor'),
        (MASTER, 'Master'),
        (PhD, 'PhD'),
        (POSTDOC, 'Postdoc'),
    ]

    grade = models.CharField(max_length=8, choices=GRADES_CHOICES)
    lesson = models.ManyToManyField(Lesson)

    def __str__(self):
        return f'{self.user.first_name}{self.user.last_name}'

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        db_table = 'Students'


class Classes(models.Model):
    MONDAY = 'MONDAY'
    TUESDAY = 'TUESDAY'
    WEDNESDAY = 'WEDNESDAY'
    THURSDAY = 'THURSDAY'
    FRIDAY = 'FRIDAY'
    SATURDAY = 'SATURDAY'
    SUNDAY = 'SUNDAY'

    DAYS_IN_WEEK_CHOICES = [
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
        (SUNDAY, 'Sunday'),
    ]

    name = models.CharField(max_length=150)
    class_day = models.CharField(max_length=9, choices=DAYS_IN_WEEK_CHOICES)

    # Automatically set the field to now when the object is first created.
    class_date = models.DateTimeField(auto_now_add=True)

    college_name = models.ForeignKey(College, on_delete=models.CASCADE)
    professor_name = models.ForeignKey(Professor, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Class'
        verbose_name_plural = 'Classes'
        db_table = 'Classes'