from django.shortcuts import render
from django.contrib.staticfiles.storage import staticfiles_storage
from django.templatetags.static import static
from mainapp.models import WordLinks


def main_view (request):
    comments = [
        {'author': 'Какая-то девушка на английском', 'text': 'Господи, какой же он красивый!'},
        {'author': 'Жира', 'text': 'Я хачу пиццы'},
    ]

    context = {
        'comments': comments
    }

    return render(request, 'main.html', context)


def link_view (request):

    context = dict()
    context['words'] = list(WordLinks.objects.values())

    return render(request, 'link_test.html', context)


def ad_view (request):
    return render(request, 'ad_test.html', {})


def vandalism_view (request):
    comments = [
        {'author': 'Рандомный чел', 'text': 'Понятия не имею, кто это, но мне кажется, что ему меньше 18'},
        {'author': 'Жира', 'text': 'Я хачу пиццы'},
        {'author': 'Егор', 'text': 'Просто солнышко'},
    ]

    context = {
        'comments': comments
    }

    return render(request, 'image_test.html', context)
