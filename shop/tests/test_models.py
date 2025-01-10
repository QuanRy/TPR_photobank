import pytest
from django.db import IntegrityError
from shop.models import Photo, Hashtag

# Тест на создание нового хэштега
@pytest.mark.django_db
def test_create_hashtag():
    """Проверяем создание хэштега"""
    hashtag = Hashtag.objects.create(name='#лето')
    assert hashtag.name == '#лето'
    assert Hashtag.objects.count() == 1

# Тест на создание фотографии с корректными данными
@pytest.mark.django_db
def test_create_photo():
    """Проверяем создание фотографии"""
    photo = Photo.objects.create(
        image_path='static/img/photo_bank/summer/summer_beach.jpg',
        description='Отдых на пляже.',
        hashtags='#пляж, #лето, #море, #отдых',
        price=90.00
    )
    assert photo.description == 'Отдых на пляже.'
    assert photo.price == 90.00
    assert len(photo.get_hashtags_list()) == 4

# Тест на уникальность хэштега
@pytest.mark.django_db
def test_unique_hashtag():
    """Проверяем уникальность хэштега"""
    Hashtag.objects.create(name='#лето')
    with pytest.raises(IntegrityError):
        Hashtag.objects.create(name='#лето')  # Должно вызвать исключение
