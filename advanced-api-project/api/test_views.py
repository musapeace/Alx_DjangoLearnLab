from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book

class BookAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Sample book data
        self.book_data = {
            "title": "Django for Beginners",
            "author": "William S. Vincent",
            "publication_year": 2018,
        }

        # Create a book instance
        self.book = Book.objects.create(**self.book_data)

    # Test Book Creation
    def test_create_book(self):
        response = self.client.post("/api/books/", self.book_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], self.book_data["title"])

    # Test Retrieving Books
    def test_get_books(self):
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    # Test Book Update
    def test_update_book(self):
        update_data = {"title": "Django Advanced", "author": "William S. Vincent"}
        response = self.client.put(f"/api/books/{self.book.id}/", update_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Django Advanced")

    # Test Book Deletion
    def test_delete_book(self):
        response = self.client.delete(f"/api/books/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    # Test Searching
    def test_search_books(self):
        response = self.client.get("/api/books/?search=Django")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    # Test Ordering
    def test_order_books(self):
        response = self.client.get("/api/books/?ordering=title")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

