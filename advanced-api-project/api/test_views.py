from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITests(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpass123")

        # Create an author
        self.author = Author.objects.create(name="Robert Martin")

        # Create sample books
        self.book1 = Book.objects.create(
            title="Clean Code",
            author=self.author,
            publication_year=2008
        )
        self.book2 = Book.objects.create(
            title="Clean Architecture",
            author=self.author,
            publication_year=2017
        )

        # Endpoint URLs
        self.list_url = reverse('book-list')  # Make sure your view name is 'book-list'
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book1.pk})

    # CRUD TESTS

    def test_list_books(self):
        # Should return a list of books
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book_authenticated(self):
        # Authenticated users should create a book
        self.client.login(username="testuser", password="testpass123")
        data = {
            "title": "Test Driven Development",
            "author": self.author.id,
            "publication_year": 2002
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        # Unauthenticated users should not create a book
        data = {
            "title": "Unauthorized Book",
            "author": self.author.id,
            "publication_year": 2025
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book(self):
        # Should update a book
        self.client.login(username="testuser", password="testpass123")
        data = {
            "title": "Clean Code Updated",
            "author": self.author.id,
            "publication_year": 2008
        }
        response = self.client.put(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Clean Code Updated")

    def test_delete_book(self):
        # Should delete a book
        self.client.login(username="testuser", password="testpass123")
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # FILTER / SEARCH / ORDER TESTS

    def test_filter_books_by_title(self):
        # Should filter books by title
        response = self.client.get(f"{self.list_url}?title=Clean Code")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Clean Code")

    def test_search_books(self):
        # Should search books by title
        response = self.client.get(f"{self.list_url}?search=Architecture")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], "Clean Architecture")

    def test_order_books_by_publication_year_desc(self):
        # Should order books by publication_year descending
        response = self.client.get(f"{self.list_url}?ordering=-publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], "Clean Architecture")
