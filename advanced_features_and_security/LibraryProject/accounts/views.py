from django.shortcuts import render
from django.contrib.auth import get_user_model
# Create your views here.

User = get_user_model()

def some_view(request):
    user = User.objects.get(id=1)
    
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User, Group
from django.http import HttpResponse

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

