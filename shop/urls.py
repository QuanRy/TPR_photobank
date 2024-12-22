from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('buy/<int:product_id>/', views.PurchaseCreate.as_view(), name='buy'),
    path('calculate_discount/', views.calculate_discount, name='calculate_discount'),
]
