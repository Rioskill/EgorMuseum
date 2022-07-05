from django.shortcuts import render
from django.contrib.staticfiles.storage import staticfiles_storage
from django.templatetags.static import static
from mainapp.models import WordLinks, Friend, FriendFact, FriendComment, LastQuestImage
from django.http import HttpResponse
from .forms import LastQuestImageForm


def main_view (request):
    comments = [
        {'author': 'Какая-то девушка на английском', 'text': 'Господи, какой же он красивый!'},
        {'author': 'Жира', 'text': 'Я хачу пиццы'},
        {'author': 'Случайный прохожий', 'text': 'Встретил его в ГУМе, выпрашивал у меня 50р, ничего ему не дал, так как принял за бомжа. Если бы у меня был второй шанс, то я поступил бы в точности так же.'}
    ]

    facts = [
        'Самый красивый человек на планете',
        'Родился 5 июля',
        'Как-то раз плакал в метро',
        'Ездил в лагерь бесчисленное количество раз',
    ]

    context = {
        'facts': facts,
        'comments': comments
    }

    return render(request, 'main.html', context)


def link_view (request):
    quests = [
        {'name': 'Массаж булок', 'img': '1.jpg'},
        {'name': 'Мемология', 'img': '2.jpg'},
        {'name': 'Ты, сука, в армии нахуй', 'img': '3.jpg'},
        {'name': 'Покупаем, докупаем, фиксируем прибыль', 'img': '4.jpg'},
    ]

    if request.method == "POST":
        form = LastQuestImageForm(request.POST, request.FILES)
        form.save()
        img_obj = form.instance

        # print(img_obj.id)
        request.session['last_image_id'] = img_obj.id

        context = {
            'quests': quests,
            'form': form,
            'img_obj': img_obj
        }

        return render(request, 'link_test.html', context)

    form = LastQuestImageForm()

    context = {
        'quests': quests,
        'form': form
    }

    if 'last_image_id' in request.session.keys():
        id = request.session['last_image_id']
        context['img_obj'] = LastQuestImage.objects.get(id=id)

    return render(request, 'link_test.html', context)


def ad_view (request):
    return render(request, 'ad_test.html', {})


def vandalism_view (request):
    if 'answers' not in request.session.keys():
        request.session['answers'] = [True for i in range(FriendFact.objects.count())]

    if 'visible_comments' not in request.session.keys():
        request.session['visible_comments'] = [i + 1 for i in range(FriendComment.objects.count())]

    if request.method == 'POST':

        request_type, body = request.body.decode('utf-8').split(': ')

        if request_type == 'checkbox':
            checkbox_id, status = body.split()
            print(checkbox_id, status)

            request.session['answers'][int(checkbox_id) - 1] = (status == 'true')
            request.session.modified = True

            print('session items:', request.session.items())

            return HttpResponse(200)
        elif request_type == 'comment':
            request.session['visible_comments'].remove(int(body))
            request.session.modified = True
            return HttpResponse(200)
        else:
            return HttpResponse(400)

    else:
        friends = list()

        checkbox_statuses = ['checked' if checkbox_status else '' for checkbox_status in request.session['answers']]

        i = 0
        for friend in Friend.objects.values():
            name = friend['name']
            facts = list(FriendFact.objects.filter(friend_id=friend['id']).values())
            comments = [comment for comment in FriendComment.objects.filter(friend_id=friend['id']).values() if comment['id'] in request.session['visible_comments']]

            facts = [{'fact': fact, 'status': status} for fact, status in zip(facts, checkbox_statuses[i:i+len(facts)])]
            i += len(facts)

            friends.append({'name': name, 'facts': facts, 'comments': comments,
                            'avatar': friend['jpeg_main'],
                            'avatar_overlay': friend['jpeg_main'].split('.')[0] + '_overlay.png'})
            print(friends[-1])

        context = {
            'friends': friends,
            'checkbox_statuses': checkbox_statuses
        }

        return render(request, 'image_test.html', context)
