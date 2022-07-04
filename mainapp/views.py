from django.shortcuts import render
from django.contrib.staticfiles.storage import staticfiles_storage
from django.templatetags.static import static
from mainapp.models import WordLinks, Friend, FriendFact, FriendComment
from django.http import HttpResponse
import json


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
    print('session items:', request.session.items())
    if request.method == 'POST':
        checkbox_id, status = request.body.decode('utf-8').split()
        print(checkbox_id, status)

        if 'answers' not in request.session.keys():
            request.session['answers'] = [True for i in range(FriendFact.objects.count())]
        request.session['answers'][int(checkbox_id)] = (status == 'true')

        print('session items:', request.session.items())

        return HttpResponse(200)

    else:
        friends = list()

        for friend in Friend.objects.values():
            # print(friend)
            name = friend['name']
            facts = list(FriendFact.objects.filter(friend_id=friend['id']).values())
            comments = list(FriendComment.objects.filter(friend_id=friend['id']).values())

            # print('friend:', friend)

            friends.append({'name': name, 'facts': facts, 'comments': comments,
                            'avatar': friend['jpeg_main'],
                            'avatar_overlay': friend['jpeg_main'].split('.')[0] + '_overlay.png'})

        # print(friends)
        # print(comments)

        context = {
            # 'comments': comments,
            'friends': friends,
            'checkbox_statuses': 
        }

        return render(request, 'image_test.html', context)
