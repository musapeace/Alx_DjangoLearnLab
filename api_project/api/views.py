from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer
'import rest_framework.generics.ListAPIView'
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class BookList(ListAPIView):
    queryset = Book.objects.all()  # Retrieve all books
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
