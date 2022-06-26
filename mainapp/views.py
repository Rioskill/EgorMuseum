from django.shortcuts import render


def main_view (request):
    return render(request, 'init.html', {})


def link_view (request):
    return render(request, 'link_test.html', {})


def ad_view (request):
    return render(request, 'ad_test.html', {})


def vandalism_view (request):
    comments = [
        {'author': 'Рандомный чел', 'text': 'Понятия не имею, кто это'},
        {'author': 'Жира', 'text': 'Я хачу пиццы'},
        {'author': 'Егор', 'text': 'Просто солнышко'},
    ]

    context = {
        'comments': comments
    }

    return render(request, 'image_test.html', context)
