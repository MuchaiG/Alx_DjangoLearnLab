from rest_framework import generics, permissions, filters
from rest_framework.exceptions import ValidationError
from django.utils import timezone
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework

# List all books – anyone can view
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Public access

    # Add search and ordering filters
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author__name', 'publication_year']  # filter by title, author name, year
    search_fields = ['title', 'author__name']  # search by book title or author name
    ordering_fields = ['title', 'publication_year']     # allow ordering by title and year
    ordering = ['publication_year']  # default ordering

# Retrieve single book – anyone can view
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  #  Public access


# Create book – only authenticated users
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Auth required

    def perform_create(self, serializer):
        # Add custom validation and logic before saving a new book.
        
        publication_year = self.request.data.get("publication_year")
        current_year = timezone.now().year

        # Prevent future publication years
        if publication_year and int(publication_year) > current_year:
            raise ValidationError("Publication year should not be in the future.")

        # Optional: Ensure an author is provided
        if not self.request.data.get("author"):
            raise ValidationError("Author is required when creating a book.")

        serializer.save()


# Update book – only authenticated users
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Auth required

    def perform_update(self, serializer):        
        #Validate and process updates before saving.
        
        publication_year = self.request.data.get("publication_year")
        current_year = timezone.now().year

        if publication_year and int(publication_year) > current_year:
            raise ValidationError("Publication year should not be in the future.")

        serializer.save()


# Delete book – only authenticated users
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Auth required
