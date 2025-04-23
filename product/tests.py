from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status

from .models import Product

# Create your tests here.
class ProductTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.product = Product.objects.create(
            name = 'Test Product',
            price = 1234.00,
            stock = 99,
        )
    
    def test_model_content(self):
        self.assertEqual(self.product.name, 'Test Product')
        self.assertEqual(self.product.price, 1234.00)
        self.assertEqual(self.product.stock, 99)

    def test_api_listview(self):
        response  = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Product.objects.count(), 1)
        self.assertContains(response, self.product.name)

    def test_api_detailview(self):
        response = self.client.get(
            reverse('product_detail', kwargs={'pk': self.product.id}),
              format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Product.objects.count(), 1)
        self.assertContains(response, 'Test Product')

    def test_search_products(self):
        response = self.client.get(
            reverse('product_list'), {'search': 'laptop'}
            )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)
        self.assertEqual(response.data, [])
