# models.py
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)


# Using select_related
from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'book_list.html', {'books': books})

#Using prefetch_related  
from django.shortcuts import render
from .models import Author

def author_list(request):
    authors = Author.objects.prefetch_related('books').all()
    return render(request, 'author_list.html', {'authors': authors})
