from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories




def index(request):

  

    context = {
        'title': 'GodSneakers - Главная',
        'content': "Магазин кроссовок GodSneakers",
       
    }

    return render(request, 'main/index.html', context)


def about(request):
    
   
    context = {
        'title': 'GodSneakers - О нас',
        'content': "О нас",
        'text_on_page': "Текст о том почему этот магазин такой классный, и какой хороший товар."
    }
   
    return render(request, 'main/about.html', context)