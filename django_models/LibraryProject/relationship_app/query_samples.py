import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')  # Replace with actual project name
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query 1: All books by a specific author
author_name = "John Doe"
books_by_author = Book.objects.filter(author__name=author_name)
print(f"Books by {author_name}:")
for book in books_by_author:
    print(book.title)

# Query 2: List all books in a library
library_name = "City Library"
try:
    library = Library.objects.get(name=library_name)
    print(f"\nBooks in {library_name}:")
    for book in library.books.all():
        print(book.title)
except Library.DoesNotExist:
    print("Library not found")

# Query 3: Retrieve the librarian for a library
try:
    librarian = Librarian.objects.get(library__name=library_name)
    print(f"\nLibrarian of {library_name}: {librarian.name}")
except Librarian.DoesNotExist:
    print("Librarian not found for this library")
