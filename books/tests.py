from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Book
from django.contrib.auth import get_user_model


class BookAPITests(APITestCase):

    def setUp(self):
        # Створення суперпользователя для тесту
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin", password="adminpassword123"
        )
        # Створення токену для суперпользователя
        self.token = RefreshToken.for_user(self.admin_user)
        self.access_token = str(self.token.access_token)

        # Створення тестових даних
        self.book_data = {
            "title": "Test Book",
            "author": "Test Author",
            "genre": "Fiction",
            "publication_year": 2024
        }

    def test_create_book(self):
        """Перевірка створення книги через API"""
        url = '/api/book/'  # URL для створення книги
        response = self.client.post(url, self.book_data, format='json',
                                    HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # Перевірка, що книга була створена

    def test_get_books(self):
        """Перевірка отримання списку книг через API"""
        url = '/api/book/'  # URL для отримання списку книг
        response = self.client.get(url, HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Перевірка, що запит успішний

    def test_get_book_by_id(self):
        """Перевірка отримання конкретної книги по ID через API"""
        # Створюємо книгу для тесту
        book = Book.objects.create(**self.book_data)
        url = f'/api/book/{book.id}/'  # URL для отримання конкретної книги
        response = self.client.get(url, HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Перевірка, що книга знайдена

    def test_update_book(self):
        """Перевірка оновлення книги через API"""
        # Створюємо книгу для тесту
        book = Book.objects.create(**self.book_data)
        url = f'/api/book/{book.id}/'  # URL для оновлення книги
        updated_data = {"title": "Updated Test Book", "author": "Updated Author", "genre": "Science",
                        "publication_year": 2025}
        response = self.client.put(url, updated_data, format='json', HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Перевірка, що книга була оновлена

    def test_delete_book(self):
        """Перевірка видалення книги через API"""
        # Створюємо книгу для тесту
        book = Book.objects.create(**self.book_data)
        url = f'/api/book/{book.id}/'  # URL для видалення книги
        response = self.client.delete(url, HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)  # Перевірка, що книга була видалена
