from django.test import TestCase
from shop.models import Product
from django.urls import reverse

class DiscountTestCase(TestCase):
    def setUp(self):
        # Создадим несколько продуктов для тестов
        self.product1 = Product.objects.create(name="Book", price=740, type="book")
        self.product2 = Product.objects.create(name="Pencil", price=50, type="stationery")
        self.product3 = Product.objects.create(name="Notebook", price=200, type="book")
        self.product4 = Product.objects.create(name="Eraser", price=30, type="stationery")
        self.product5 = Product.objects.create(name="Pen", price=10, type="stationery")

    def test_calculate_discount(self):
        response = self.client.post(reverse('calculate_discount'), {'cart': ['1', '2', '3']})
        data = response.json()

        # Преобразуем ID в строку
        self.assertEqual(data['discounted_prices'][str(self.product1.id)], 740)  # Без скидки
        self.assertEqual(data['discounted_prices'][str(self.product2.id)], 50)   # Без скидки
        self.assertEqual(data['discounted_prices'][str(self.product3.id)], 120.0)  # Скидка
