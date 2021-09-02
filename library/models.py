from django.db import models
from university.models import College, Student, Major


class Book(models.Model):
    name = models.CharField(max_length=150)
    major = models.ForeignKey(Major, on_delete=models.CASCADE)
    is_in_rent = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        db_table = 'Books'

class Rent(models.Model):
    book_name = models.ForeignKey(Book, on_delete=models.CASCADE)
    student_name = models.ForeignKey(Student, on_delete=models.CASCADE)
    # Automatically set the field to now when the object is first created.
    rent_start_date = models.DateTimeField(auto_now_add=True)
    rent_end_date = models.DateTimeField()

    def __str__(self):
        return f'{self.book_name}'

    class Meta:
        verbose_name = 'Rent'
        verbose_name_plural = 'Rents'
        db_table = 'Rents'