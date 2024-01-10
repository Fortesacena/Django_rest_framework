from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import Book

# Using a function-based view
# def book_list(request):
#     books = Book.objects.all()
#     return render(request, 'books.html', {'books': books})

# Using a class-based view
class BookListView(ListView):
    model = Book
    template_name = 'books.html'
    context_object_name = 'books'
