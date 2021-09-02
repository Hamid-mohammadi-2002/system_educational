from django.urls import path
from .views import BooksListView, rent_book

app_name = 'library'

urlpatterns = [
    path('', BooksListView.as_view(), name='books_list'),
    path('rent/<int:book_id>/', rent_book, name='rent_book'),
]
