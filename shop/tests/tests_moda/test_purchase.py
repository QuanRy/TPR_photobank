from django.test import TestCase
from shop.models import Product, Purchase
from datetime import datetime


class PurchaseTestCase(TestCase):
    def setUp(self):
        self.product_book = Product.objects.create(name="book", price=740, type="stationery")
        self.product_pencil = Product.objects.create(name="pencil", price=50, type="stationery")
        self.purchase = Purchase.objects.create(product=self.product_book,
                                                person="Ivanov",
                                                address="Svetlaya St.")

    def test_correctness_types(self):
        # Проверяем, что поля модели Purchase имеют правильный тип
        purchase = self.purchase
        self.assertIsInstance(purchase.person, str)
        self.assertIsInstance(purchase.address, str)
        self.assertIsInstance(purchase.date, datetime)

    def test_correctness_data(self):
        # Проверяем, что данные покупки корректны
        purchase = self.purchase
        self.assertEqual(purchase.person, "Ivanov")
        self.assertEqual(purchase.address, "Svetlaya St.")
        self.assertEqual(purchase.product.name, "book")
        self.assertTrue(purchase.date.replace(microsecond=0) == datetime.now().replace(microsecond=0))

