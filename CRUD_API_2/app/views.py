from django.shortcuts import render
from rest_framework.response import Response

# Create your views here.
from rest_framework import generics

from app.models import Book
from app.serializers import BookSerializer


class CreateViewBook(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def perform_create(self, serializer):
        author = self.request.user
        serializer.save(author=author)


class UpdateDeleteBook(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
