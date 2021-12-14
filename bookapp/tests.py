from django.test import TestCase
from django.db import IntegrityError, OperationalError
from rest_framework.test import APITestCase
from rest_framework import status


from .models import Book
# Create your tests here.

class BookModelTest(APITestCase):

    def test_book_created_with_correct_data(self):
        """
        it is not disallowed to create admin user without company id.
        """
        
        response = self.client.post('/authors/',{'first_name':'Maria', 'last_name':"Anna"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.post('/books/',{'title':'Book Title A', 'stock': 5, 'author':response.json()['id']})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_book_not_created_with_wrong_author_id(self):
        """
        create CustomerUser succesfully.
        """
        response = self.client.post('/authors/',{'first_name':'Maria', 'last_name':"Anna"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.post('/books/',{'title':'Book Title A', 'stock': 5, 'author':response.json()['id'] + 1})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_book_response_with_author_name(self):
        """
        create CustomerUser succesfully.
        """
        response = self.client.post('/authors/',{'first_name':'Maria', 'last_name':"Anna"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        response = self.client.post('/books/',{'title':'Book Title A', 'stock': 5, 'author':response.json()['id']})
        book_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(book_data['author_name'], "Maria Anna")
