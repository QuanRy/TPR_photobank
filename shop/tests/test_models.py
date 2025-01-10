from django.test import TestCase
from shop.models import Photo, Hashtag


class PhotoModelTests(TestCase):
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

    def test_photo_creation(self):
        # Проверяем, что фотографии были созданы
        self.assertEqual(Photo.objects.count(), 2)

    def test_photo_get_hashtags_list(self):
        # Проверяем работу метода get_hashtags_list
        hashtags_list = self.photo1.get_hashtags_list()
        self.assertEqual(hashtags_list, ['#праздник', '#новыйгод'])

    def test_photo_price(self):
        # Проверяем цену
        self.assertEqual(self.photo2.price, 300.00)

    def test_photo_description(self):
        # Проверяем описание фотографии
        self.assertEqual(self.photo1.description, 'New Year Celebration')


class HashtagModelTests(TestCase):
    def setUp(self):
        # Создаем хэштеги
        self.hashtag1 = Hashtag.objects.create(name='#праздник')
        self.hashtag2 = Hashtag.objects.create(name='#лето')

    def test_hashtag_creation(self):
        # Проверяем создание хэштегов
        self.assertEqual(Hashtag.objects.count(), 2)

    def test_hashtag_name(self):
        # Проверяем имя хэштега
        self.assertEqual(self.hashtag1.name, '#праздник')
        self.assertEqual(self.hashtag2.name, '#лето')
