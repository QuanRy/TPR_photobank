from django.test import TestCase, Client
from shop.models import Photo
from django.urls import reverse


class PhotoControllerTests(TestCase):
    def setUp(self):
        # Создаем фотографии
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
        self.client = Client()

    def test_photo_list_view(self):
        # Получаем страницу списка фотографий
        response = self.client.get(reverse('photo_list'))
        self.assertEqual(response.status_code, 200)

    def test_search_photos_view(self):
        # Тестируем поиск по хэштегу
        response = self.client.get(reverse('search_photos'), {'hashtag': '#лето'})
        self.assertEqual(response.status_code, 200)
