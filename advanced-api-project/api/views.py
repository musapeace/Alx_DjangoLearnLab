from django.shortcuts import render
from django_filters import rest_framework
from rest_framework import generics
from rest_framework import filters
from .models import Author, Book
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import AuthorSerializer, BookSerializer
"from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated", "IsAuthenticated"
["ListView", "DetailView", "UpdateView", "DeleteView"]

class AuthorListCreateView(generics.ListCreateAPIView):
    """API endpoint for listing and creating authors."""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookListCreateView(generics.ListCreateAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author__name', 'publication_year']
    search_fields = ['title', 'author__name']

    
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['title', 'author', 'publication_year']

    search_fields = ['title', 'author']


    ordering_fields = ['title', 'publication_year']


class BookDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer