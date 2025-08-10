from django.urls import path
from .views import BookList

urlpatterns = [
    path("api/books", BookList.as_view(), name="book_list_create"),
]