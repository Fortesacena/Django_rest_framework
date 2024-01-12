from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from books.models import Book

class BookListView(ListView):
    model = Book
    template_name = 'books.html'
    context_object_name = 'books'
