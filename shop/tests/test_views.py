from django.test import TestCase, Client
from shop.models import Photo
from django.urls import reverse


class PhotoViewTests(TestCase):
    def setUp(self):
        # Создаем несколько фотографий для тестов
        self.photo1 = Photo.objects.create(
            image_path='path/to/photo1.jpg',
            description='New Year Celebration',
            hashtags='#праздник, #новыйгод',
            price=500.00
        )
        self.photo2 = Photo.objects.create(
            image_path='path/to/photo2.jpg',
            description='Summer Vacation',
            hashtags='#лето',
            price=300.00
        )
        self.photo3 = Photo.objects.create(
            image_path='path/to/photo3.jpg',
            description='City Landscape',
            hashtags='#город',
            price=150.00
        )
        self.client = Client()

    def test_1_photo_list_view(self):
        """
        Тестирует страницу списка фотографий.
        Проверяет, что фотографии отображаются на странице с кодом ответа 200.
        """
        response = self.client.get(reverse('photo_list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New Year Celebration')
        self.assertContains(response, 'Summer Vacation')
        self.assertContains(response, 'City Landscape')

    def test_2_search_photos_view(self):
        """
        Тестирует поиск по хэштегу.
        Проверяет, что поиск по хэштегу #лето возвращает только фотографии с этим хэштегом.
        """
        response = self.client.get(reverse('search_photos'), {'hashtag': '#лето'})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Summer Vacation')
        self.assertNotContains(response, 'New Year Celebration')
        self.assertNotContains(response, 'City Landscape')

        # Тестируем поиск с пустым хэштегом
        response_empty = self.client.get(reverse('search_photos'), {'hashtag': ''})

        self.assertEqual(response_empty.status_code, 200)
        self.assertContains(response_empty, 'Фото не найдено')
