from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.detail import DetailView
from .models import Book, Library
from django.contrib.auth import login

# Function-based view to list all books
def list_books(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'list_books.html', {'books': books})

# Class-based view to show details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # or wherever you want to redirect
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
