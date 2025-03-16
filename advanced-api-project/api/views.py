from django.shortcuts import render

from rest_framework import generics
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

class AuthorListCreateView(generics.ListCreateAPIView):
    """API endpoint for listing and creating authors."""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookListCreateView(generics.ListCreateAPIView):
    """API endpoint for listing and creating books."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer

