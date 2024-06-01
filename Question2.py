from django.db.models import Q
from django.shortcuts import render
from .models import Book

def search_books(request):
    # Creating a Q object for complex queries
    query = Q(title__startswith='Django') | Q(author__name='John')
    # Filtering books based on the Q object
    books = Book.objects.filter(query)
    return render(request, 'search_results.html', {'books': books})
