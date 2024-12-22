from django.test import TestCase
from django.urls import reverse
from shop.models import Product


class ViewsTestCase(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name="book", price=740, type="stationery")

    def test_index_view(self):
        # Проверяем, что главная страница возвращает правильный контекст
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('products', response.context)
        self.assertEqual(len(response.context['products']), 1)

    def test_purchase_create_view(self):
        # Проверяем, что страница покупки товара работает корректно
        response = self.client.get(reverse('buy', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'form')
        self.assertContains(response, 'person')
        self.assertContains(response, 'address')

        # Проверяем создание покупки через форму
        response = self.client.post(reverse('buy', args=[self.product.id]), {
            'person': 'Ivanov',
            'address': 'Svetlaya St.',
            'product': self.product.id
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Спасибо за покупку, Ivanov!')
