from rest_framework import serializers
from .models import Book, Author
from django.utils import timezone

# Book serializer
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_year']

    # Custom validation for published_year
    def validate_published_year(self, value):
        current_year = timezone.now().year
        if value > current_year:
            raise serializers.ValidationError("Published year should not be in the future.")
        return value

# Author serializer with nested books
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']

    