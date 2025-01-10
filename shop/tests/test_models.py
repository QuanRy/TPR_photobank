from django.test import TestCase
from shop.models import Photo, Hashtag


class PhotoModelTests(TestCase):
    def setUp(self):
        # Создаем фотографии для тестов
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

    def test_1_photo_creation(self):
        """
        Тестирует создание фотографий.
        Проверяет, что фотографии созданы корректно.
        """
        self.assertEqual(Photo.objects.count(), 2)

    def test_2_photo_get_hashtags_list(self):
        """
        Тестирует метод get_hashtags_list для фотографии.
        Проверяет, что метод возвращает правильный список хэштегов.
        """
        hashtags_list = self.photo1.get_hashtags_list()
        self.assertEqual(hashtags_list, ['#праздник', '#новыйгод'])

    def test_3_photo_price(self):
        """
        Тестирует цену фотографии.
        Проверяет, что цена фотографии установлена корректно.
        """
        self.assertEqual(self.photo2.price, 300.00)

    def test_4_photo_description(self):
        """
        Тестирует описание фотографии.
        Проверяет, что описание фотографии установлено корректно.
        """
        self.assertEqual(self.photo1.description, 'New Year Celebration')


class HashtagModelTests(TestCase):
    def setUp(self):
        # Создаем хэштеги для тестов
        self.hashtag1 = Hashtag.objects.create(name='#праздник')
        self.hashtag2 = Hashtag.objects.create(name='#лето')

    def test_1_hashtag_creation(self):
        """
        Тестирует создание хэштегов.
        Проверяет, что хэштеги были созданы.
        """
        self.assertEqual(Hashtag.objects.count(), 2)

    def test_2_hashtag_name(self):
        """
        Тестирует имена хэштегов.
        Проверяет, что хэштеги имеют правильные имена.
        """
        self.assertEqual(self.hashtag1.name, '#праздник')
        self.assertEqual(self.hashtag2.name, '#лето')
