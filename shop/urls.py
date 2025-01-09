from django.urls import path
from . import views


urlpatterns = [
    path('', views.photo_list, name='index'),  # Главная страница (будет обрабатывать путь '/')
    path('photos/', views.photo_list, name='photo_list'),  # Страница с фотографиями
    path('search/', views.search_photos, name='search_photos'),
]