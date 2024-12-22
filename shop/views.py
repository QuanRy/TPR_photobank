from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic.edit import CreateView

from .models import Product, Purchase

# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shop/index.html', context)


def calculate_discount(request):
    if request.method == "POST":
        cart = request.POST.getlist('cart')  # Получаем корзину из запроса
        cart_data = [int(item) for item in cart]  # Преобразуем в список ID товаров

        # Считаем количество типов в корзине
        products = Product.objects.filter(id__in=cart_data)
        types_in_cart = list(set(products.values_list('type', flat=True)))

        is_discount_applicable = len(types_in_cart) >= 2 and len(cart_data) == 3

        # Рассчитываем итоговую сумму и цены с учетом скидки
        total_price = 0
        discounted_prices = {}
        for index, product in enumerate(products):
            if index == 2 and is_discount_applicable:
                discounted_price = product.price * 0.6  # Применяем скидку для третьего товара
            else:
                discounted_price = product.price
            discounted_prices[str(product.id)] = discounted_price  # Преобразуем ID в строку
            total_price += discounted_price

        return JsonResponse({'total_price': total_price, 'discounted_prices': discounted_prices})

    return JsonResponse({'error': 'Неверный метод запроса'}, status=400)



class PurchaseCreate(CreateView):
    model = Purchase
    fields = ['product', 'person', 'address']

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponse(f'Спасибо за покупку, {self.object.person}!')

