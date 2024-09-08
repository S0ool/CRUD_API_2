from rest_framework import serializers

from app.models import Book


class BookSerializer(serializers.ModelSerializer):
    author = serializers.CharField(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'
