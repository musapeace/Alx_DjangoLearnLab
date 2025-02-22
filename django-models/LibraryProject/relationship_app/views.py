<<<<<<< HEAD
from django.views.generic.detail import DetailView
from .models import Library
from django.views.generic.detail import DetailView
=======
from .models import Library
>>>>>>> b34957c31e466f90cadc1ef483824f0b06b11f1e
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# Function-Based View (FBV) - Lists all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-Based View (CBV) - Displays details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
