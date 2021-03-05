from rest_framework import serializers
from nsApp.books.models import Book
from nsApp.author.models import Author
from nsApp.books.serializers import BookSerializer


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(read_only=True, many=True)

    class Meta:
        model = Author
        fields = "__all__"
