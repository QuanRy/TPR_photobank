from django.test import TestCase
from shop.models import Product


class ProductTestCase(TestCase):
    def setUp(self):
        # Создаем два продукта для тестирования
        self.product1 = Product.objects.create(name="book", price=740, type="stationery")
        self.product2 = Product.objects.create(name="pencil", price=50, type="stationery")

    def test_correctness_types(self):
        # Проверяем, что типы данных правильные
        self.assertIsInstance(self.product1.name, str)
        self.assertIsInstance(self.product1.price, int)
        self.assertIsInstance(self.product2.name, str)
        self.assertIsInstance(self.product2.price, int)

    def test_correctness_data(self):
        # Проверяем, что данные правильные
        self.assertEqual(self.product1.price, 740)
        self.assertEqual(self.product2.price, 50)

    def test_calculate_discounted_price(self):
        # Проверяем, что метод расчета скидки работает
        self.assertEqual(self.product1.calculate_discounted_price(True), 444)  # 740 * 0.6 = 444
        self.assertEqual(self.product1.calculate_discounted_price(False), 740)
