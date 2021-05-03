from django.shortcuts import render


# Create your views here.
def index(request):
    context = {'page_title': 'главная',}
    return render(request, 'mainapp/index.html', context)


def contacts(request):
    contact_list = [
        {'city': 'Москва',
         'phone': '+7-888-888-8888',
         'email': 'info@geekshop.ru',
         'address': 'В пределах МКАД'},
        {'city': 'Саратов',
         'phone': '+7-888-888-8888',
         'email': 'info@geekshop.ru',
         'address': 'В пределах МКАД'},
        {'city': 'Сочи',
         'phone': '+7-888-888-8888',
         'email': 'info@geekshop.ru',
         'address': 'В пределах МКАД'},
    ]
    context = {'page_title': 'контакты',
               'contact_list': contact_list,}
    return render(request, 'mainapp/contact.html', context)


def products(request):
    product_list = ['все', 'дом', 'офис', 'модерн', 'классика']
    context = {'page_title': 'каталог',
               'product_list': product_list}
    return render(request, 'mainapp/products.html', context)
