from django.shortcuts import render
from nsApp.books.models import Book
from nsApp.books.serializers import BookSerializer
from rest_framework import generics

class ListBook(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class DetailBook(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

