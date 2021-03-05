from rest_framework import serializers
from nsApp.books.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['author', 'date_publication', 'edition_number']