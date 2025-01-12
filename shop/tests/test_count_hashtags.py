import json
from django.urls import reverse
from django.test import TestCase
from shop.models import Photo

class StatisticsTest(TestCase):
    
    def setUp(self):
        self.photo1 = Photo.objects.create(
            image_path='path/to/photo1.jpg',
            description='Nature Sunset',
            hashtags='nature, sunset',
            price=10.00
        )
        self.photo2 = Photo.objects.create(
            image_path='path/to/photo2.jpg',
            description='Beach Vacation',
            hashtags='nature, beach',
            price=20.00
        )
        self.photo3 = Photo.objects.create(
            image_path='path/to/photo3.jpg',
            description='City View',
            hashtags='sunset, ocean',
            price=15.00
        )

    def test_hashtag_count(self):
        """
        Тестирует правильность подсчета хэштегов при фильтрации.
        """
        # Тест с хэштегом 'nature'
        response = self.client.get(reverse('search_photos') + '?hashtag=nature')
        
        # Проверяем, что ответ успешный
        self.assertEqual(response.status_code, 200)
        
        # Проверяем подсчет хэштегов для 'nature'
        hashtag_data = response.context['hashtag_data']
        hashtag_data = json.loads(hashtag_data)
        
        # Ожидаем, что хэштег 'nature' будет встречаться дважды
        hashtag_counts = {entry['hashtag']: entry['count'] for entry in hashtag_data}
        self.assertEqual(hashtag_counts['nature'], 2)
        
        # Проверяем, что фото с хэштегом 'nature' отобразятся
        self.assertContains(response, 'nature')
        self.assertContains(response, 'sunset')
        self.assertContains(response, 'beach')

    def test_hashtag_empty_search(self):
        """
        Тестирует правильность работы функции поиска при отсутствии хэштега.
        """
        # Тест без хэштега
        response = self.client.get(reverse('search_photos'))
        
        # Проверяем, что ответ успешный
        self.assertEqual(response.status_code, 200)
        
        # Проверяем, что все фотографии отобразились
        self.assertContains(response, 'nature')
        self.assertContains(response, 'sunset')
        self.assertContains(response, 'beach')
        self.assertContains(response, 'ocean')