from django.shortcuts import render
from .models import *
# Create your views here.

def list_books(request):
    books = Book.objects.all()
    return render(request,'relationship_app/book_list.html',{'books':books})
