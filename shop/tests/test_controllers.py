import pytest
from django.urls import reverse
from shop.models import Photo

@pytest.mark.django_db
def test_purchase_view(client):
    """Тестируем страницу покупки фотографии"""
    photo = Photo.objects.create(
        image_path='static/img/photo_bank/summer/summer_beach.jpg',
        description='Отдых на пляже.',
        hashtags='#пляж, #лето, #море, #отдых',
        price=90.00
    )
    url = reverse('purchase_view') + f'?photo_id={photo.id}'
    response = client.get(url)
    
    assert response.status_code == 200
    assert 'photo' in response.context
    assert response.context['photo'] == photo

@pytest.mark.django_db
def test_statistics_view(client):
    """Тестируем страницу статистики"""
    Photo.objects.create(
        image_path='static/img/photo_bank/summer/summer_beach.jpg',
        description='Отдых на пляже.',
        hashtags='#пляж, #лето, #море, #отдых',
        price=90.00
    )
    url = reverse('statistics_view')
    response = client.get(url)
    
    assert response.status_code == 200
    assert 'price_histogram' in response.context
    assert 'hashtag_pie' in response.context
    assert 'category_pie' in response.context
