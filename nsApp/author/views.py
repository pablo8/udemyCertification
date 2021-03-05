from django.shortcuts import render
from rest_framework import generics
from nsApp.author.models import Author
from nsApp.author.serializers import AuthorSerializer


class ListAuthor(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class DetailAuthor(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

