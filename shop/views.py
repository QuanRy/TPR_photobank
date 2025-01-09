from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic.edit import CreateView

from django.shortcuts import render
from .models import Photo

def photo_list(request):
    # Хэштеги для каждой категории
    new_year_tags = ['#праздник', '#новыйгод', '#рождество']
    summer_tags = ['#лето']
    cities_tags = ['#город']

    # Получаем все фотографии
    photos = Photo.objects.all()

    # Фильтрация по категориям с проверкой хэштегов
    new_year_photos = [photo for photo in photos if any(tag in photo.get_hashtags_list() for tag in new_year_tags)]
    summer_photos = [photo for photo in photos if any(tag in photo.get_hashtags_list() for tag in summer_tags)]
    cities_photos = [photo for photo in photos if any(tag in photo.get_hashtags_list() for tag in cities_tags)]

    # Отправляем в шаблон
    return render(request, 'shop/index.html', {
        'new_year_photos': new_year_photos,
        'summer_photos': summer_photos,
        'cities_photos': cities_photos,
    })