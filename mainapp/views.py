from django.shortcuts import render
from django.contrib.staticfiles.storage import staticfiles_storage
from django.templatetags.static import static
from mainapp.models import WordLinks


def main_view (request):
    return render(request, 'init.html', {})


def link_view (request):

    context = {}

    # print(WordLinks.objects.values())

    context['words'] = list(WordLinks.objects.values())

    # words = [{'word': word, 'ref': ref} for word, ref in WordLinks.objects.values()]

    # context['words'] = words
    # with open(static('links.WordLinks.objects.values()txt'), 'r') as file:
    #     lines = file.readlines()
    #     context['words'] = [{'word': word, 'ref': ref} for word, ref in map(lambda x: x.split(), lines)]

    # print(context)
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
