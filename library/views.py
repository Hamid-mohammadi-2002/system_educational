from django.shortcuts import render
from django.views.generic import ListView
from library.models import Book


class BooksListView(ListView):
    context_object_name = 'Classes'
    queryset = Book.objects.filter(is_in_rent=True)
    template_name = 'library/books_list.html'


def rent_book(request, pk):
    pass
