from django.test import TestCase
from shop.models import Product
from django.urls import reverse

class DiscountTestCase(TestCase):     

    def test_calculate_discount(self):
        # Создадим несколько продуктов для тестов
        self.product1 = Product.objects.create(name="Book", price=740, type="book")
        self.product2 = Product.objects.create(name="Pencil", price=50, type="stationery")
        self.product3 = Product.objects.create(name="Notebook", price=200, type="book")
        self.product4 = Product.objects.create(name="Eraser", price=30, type="stationery")
        self.product5 = Product.objects.create(name="Pen", price=10, type="stationery")

        response = self.client.post(reverse('calculate_discount'), {'cart': ['1', '2', '3']})
        data = response.json()

        # Преобразуем ID в строку
        self.assertEqual(data['discounted_prices'][str(self.product1.id)], 740)  # Без скидки
        self.assertEqual(data['discounted_prices'][str(self.product2.id)], 50)   # Без скидки
        self.assertEqual(data['discounted_prices'][str(self.product3.id)], 120.0)  # Скидка


    # В файле test_discount.py
    def test_discount_only_for_3_items_and_2_types(self):
        # Создаем продукты
        self.product1 = Product.objects.create(name="Book", price=740, type="book")
        self.product2 = Product.objects.create(name="Pencil", price=50, type="stationery")
        self.product3 = Product.objects.create(name="Eraser", price=30, type="stationery")
        self.product4 = Product.objects.create(name="Notebook", price=200, type="book")

        # Тестируем, что скидка применяется
        response = self.client.post(reverse('calculate_discount'), {'cart': [self.product1.id, self.product2.id, self.product3.id]})
        data = response.json()
        self.assertTrue(data['discounted_prices'][str(self.product3.id)] < self.product3.price)  # Скидка должна быть на третий товар

        # Проверка, что скидка не применяется, если в корзине меньше 3 товаров или недостаточно типов
        response = self.client.post(reverse('calculate_discount'), {'cart': [self.product1.id, self.product2.id]})
        data = response.json()
        self.assertEqual(data['discounted_prices'][str(self.product1.id)], self.product1.price)  # Без скидки
        self.assertEqual(data['discounted_prices'][str(self.product2.id)], self.product2.price)  # Без скидки


    # В файле test_discount.py
    def test_discount_applies_correctly_with_various_combinations(self):
        # Создаем продукты
        self.product1 = Product.objects.create(name="Book", price=740, type="book")
        self.product2 = Product.objects.create(name="Pencil", price=50, type="stationery")
        self.product3 = Product.objects.create(name="Eraser", price=30, type="stationery")
        self.product4 = Product.objects.create(name="Notebook", price=200, type="book")

        # Комбинация с 3 товарами и разными типами
        response = self.client.post(reverse('calculate_discount'), {'cart': [self.product1.id, self.product2.id, self.product3.id]})
        data = response.json()
        self.assertTrue(data['discounted_prices'][str(self.product3.id)] < self.product3.price)  # Скидка на третий товар

        # Комбинация из 3 товаров одного типа (без скидки)
        response = self.client.post(reverse('calculate_discount'), {'cart': [self.product1.id, self.product4.id, self.product1.id]})
        data = response.json()
        self.assertEqual(data['discounted_prices'][str(self.product1.id)], self.product1.price)  # Без скидки


    # В файле test_calculate_discount.py
    def test_price_without_discount_is_correct(self):
        # Создаем продукты
        self.product1 = Product.objects.create(name="Book", price=740, type="book")
        self.product2 = Product.objects.create(name="Pencil", price=50, type="stationery")
        self.product3 = Product.objects.create(name="Eraser", price=30, type="stationery")

        # Отправляем запрос на корзину без скидки
        response = self.client.post(reverse('calculate_discount'), {'cart': [self.product1.id, self.product2.id]})
        data = response.json()

        # Проверяем, что товары без скидки остаются по той же цене
        self.assertEqual(data['discounted_prices'][str(self.product1.id)], self.product1.price)
        self.assertEqual(data['discounted_prices'][str(self.product2.id)], self.product2.price)

