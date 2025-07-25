# relationship_app/query_samples.py

import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')  # Replace with your project name
django.setup()

from relationship_app.models import Author, Book, Library

# 1. Query all books by a specific author
author_name = "John Doe"
try:
    author = Author.objects.get(name=author_name)
    books_by_author = author.books.all()
    print(f"Books by {author.name}:")
    for book in books_by_author:
        print(f"- {book.title}")
except Author.DoesNotExist:
    print(f"No author found with the name '{author_name}'")

# 2. List all books in a library
library_name = "Central Library"
try:
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()
    print(f"\nBooks in {library.name}:")
    for book in books_in_library:
        print(f"- {book.title} by {book.author.name}")
except Library.DoesNotExist:
    print(f"No library found with the name '{library_name}'")

# 3. Retrieve the librarian for a library
try:
    librarian = library.librarian  # Uses OneToOne relationship
    print(f"\nLibrarian for {library.name}: {librarian.name}")
except AttributeError:
    print(f"No librarian assigned to {library.name}")
