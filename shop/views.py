from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic.edit import CreateView

from django.shortcuts import render
from .models import Photo

def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'shop/index.html', {'photos': photos})