from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic.edit import CreateView

from django.shortcuts import render, get_object_or_404
from .models import Photo, Hashtag
from io import BytesIO
import pandas as pd
import matplotlib.pyplot as plt



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



def search_photos(request):
    hashtag = request.GET.get('hashtag', '')  # Получаем хэштег из параметров запроса

    if hashtag:
        # Фильтруем фотографии по хэштегу, сравнивая с хэш-тегами каждой фотографии
        photos = Photo.objects.filter(hashtags__icontains=hashtag)
    else:
        photos = []  # Если хэштег не указан, показываем пустой список

    return render(request, 'shop/search_results.html', {
        'hashtag': hashtag,
        'photos': photos
    })



def purchase_view(request):
    # Получаем photo_id из GET-запроса
    photo_id = request.GET.get('photo_id')
    if not photo_id:
        return HttpResponse("Ошибка: не указан ID фотографии.", status=400)

    try:
        # Пытаемся получить объект фото по переданному ID
        photo = get_object_or_404(Photo, id=photo_id)
    except Exception as e:
        print(f"Ошибка при получении фото с id {photo_id}: {str(e)}")
        return HttpResponse(status=500)

    return render(request, 'shop/purchase.html', {'photo': photo})




def statistics_view(request):
    # Новогодние, летние и городские теги
    new_year_tags = ['#праздник', '#новыйгод', '#рождество']
    summer_tags = ['#лето']
    cities_tags = ['#город']

    # Извлекаем все фотографии
    photos = Photo.objects.all()

    # Создаем pandas DataFrame из данных фотографий
    data = {
        'price': [photo.price for photo in photos],
        'hashtags': [photo.get_hashtags_list() for photo in photos],
    }
    df = pd.DataFrame(data)

    # Строим гистограмму по ценам
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(df['price'], bins=20, color='blue', alpha=0.7)
    ax.set_title('Гистограмма цен на фотографии')
    ax.set_xlabel('Цена')
    ax.set_ylabel('Количество')

    # Сохраняем график в изображение
    img_stream = BytesIO()
    plt.savefig(img_stream, format='png')
    img_stream.seek(0)

    # Строим pie диаграмму для хэштегов
    hashtag_counts = {}
    for hashtags in df['hashtags']:
        for tag in hashtags:
            hashtag_counts[tag] = hashtag_counts.get(tag, 0) + 1
    hashtag_df = pd.DataFrame(list(hashtag_counts.items()), columns=['Hashtag', 'Count'])

    fig2, ax2 = plt.subplots(figsize=(8, 8))
    ax2.pie(hashtag_df['Count'], labels=hashtag_df['Hashtag'], autopct='%1.1f%%', startangle=90)
    ax2.set_title('Распределение хэштегов по фотографиям')

    hashtag_img_stream = BytesIO()
    plt.savefig(hashtag_img_stream, format='png')
    hashtag_img_stream.seek(0)

    # Строим диаграмму по категориям (новогодние, летние, городские фотографии)
    category_counts = {
        'New Year': len([photo for photo in photos if any(tag in photo.get_hashtags_list() for tag in new_year_tags)]),
        'Summer': len([photo for photo in photos if any(tag in photo.get_hashtags_list() for tag in summer_tags)]),
        'Cities': len([photo for photo in photos if any(tag in photo.get_hashtags_list() for tag in cities_tags)]),
    }

    fig3, ax3 = plt.subplots(figsize=(8, 8))
    ax3.pie(category_counts.values(), labels=category_counts.keys(), autopct='%1.1f%%', startangle=90)
    ax3.set_title('Распределение фотографий по категориям')

    category_img_stream = BytesIO()
    plt.savefig(category_img_stream, format='png')
    category_img_stream.seek(0)

    # Передаем все изображения и графики в шаблон
    return render(request, 'shop/statistics.html', {
        'price_histogram': img_stream,
        'hashtag_pie': hashtag_img_stream,
        'category_pie': category_img_stream,
    })