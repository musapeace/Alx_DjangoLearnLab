from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer
import rest_framework.generics.ListAPIView

class BookList(ListAPIView):
    queryset = Book.objects.all()  # Retrieve all books
    serializer_class = BookSerializer 
