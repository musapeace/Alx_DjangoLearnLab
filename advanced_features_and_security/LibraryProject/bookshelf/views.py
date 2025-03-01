from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from .models import Book  # Ensure your model is imported

def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})


@permission_required('accounts.can_view', raise_exception=True)
def view_records(request):
    return HttpResponse("You have permission to view records.")

@permission_required('accounts.can_create', raise_exception=True)
def create_record(request):
    return HttpResponse("You have permission to create records.")

@permission_required('accounts.can_edit', raise_exception=True)
def edit_record(request):
    return HttpResponse("You have permission to edit records.")

@permission_required('accounts.can_delete', raise_exception=True)
def delete_record(request):
    return HttpResponse("You have permission to delete records.")

