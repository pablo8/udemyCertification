from django.db import models
from nsApp.author.models import Author


class Book(models.Model):
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    date_publication = models.DateTimeField(blank=True)
    edition_number = models.IntegerField(blank=True)
