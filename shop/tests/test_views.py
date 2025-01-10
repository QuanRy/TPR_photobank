import pytest
from django.urls import reverse
from shop.models import Photo

@pytest.mark.django_db
def test_photo_list_view(client):
    """Тестируем отображение списка фотографий"""
    Photo.objects.create(
        image_path='static/img/photo_bank/summer/summer_beach.jpg',
        description='Отдых на пляже.',
        hashtags='#пляж, #лето, #море, #отдых',
        price=90.00
    )
    url = reverse('photo_list')
    response = client.get(url)
    
    assert response.status_code == 200
    assert 'new_year_photos' in response.context
    assert 'summer_photos' in response.context
    assert 'cities_photos' in response.context

@pytest.mark.django_db
def test_search_photos_view(client):
    """Тестируем поиск фотографий по хэштегу"""
    photo = Photo.objects.create(
        image_path='static/img/photo_bank/summer/summer_beach.jpg',
        description='Отдых на пляже.',
        hashtags='#пляж, #лето, #море, #отдых',
        price=90.00
    )
    url = reverse('search_photos') + '?hashtag=%23лето'
    response = client.get(url)
    
    assert response.status_code == 200
    assert 'photos' in response.context
    assert len(response.context['photos']) == 1
    assert response.context['photos'][0] == photo

@pytest.mark.django_db
def test_invalid_search_photos_view(client):
    """Тестируем поиск с некорректным хэштегом"""
    url = reverse('search_photos') + '?hashtag=%23несуществующий'
    response = client.get(url)
    
    assert response.status_code == 200
    assert 'photos' in response.context
    assert len(response.context['photos']) == 0
