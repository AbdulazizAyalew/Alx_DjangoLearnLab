from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)  # Store author name

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)  # Book title
    publication_year = models.IntegerField()  # Year of publication
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    # One Author can have many Books

    def __str__(self):
        return self.title