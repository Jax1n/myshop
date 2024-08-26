from django.shortcuts import render


def index(request):
    context: dict[str, str] = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
    }

    return render(request, 'index.html', context)

def about(request):
    context: dict[str, str] = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст о том почему этот магазин такой классный и какой хороший товар'
    }

    return render(request, 'about.html', context)