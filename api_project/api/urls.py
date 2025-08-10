from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path("api/books", BookList.as_view(), name="book_list_create"),
    path('', include(router.urls)),
]