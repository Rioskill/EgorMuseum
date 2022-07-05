from django.db import models


class WordLinks(models.Model):
    word = models.CharField(max_length=50)
    href = models.CharField(max_length=150)


class Friend(models.Model):
    name = models.CharField(max_length=50)
    jpeg_main = models.ImageField(default=None, upload_to='avatars/', height_field=None, width_field=None)
    # png_over = models.ImageField()


class FriendFact(models.Model):
    friend = models.ForeignKey(to=Friend, unique=False, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)


class FriendComment(models.Model):
    friend = models.ForeignKey(to=Friend, unique=False, on_delete=models.CASCADE)
    author = models.CharField(max_length=100, null=True)
    text = models.CharField(max_length=300, null=True)


class LastQuestImage(models.Model):
    image = models.ImageField(upload_to='images')

# class FriendFactAnswer(models.Model):
#     user =
#     fact = models.ForeignKey(to=FriendFact, on_delete=models.CASCADE)
#     checked = models.BooleanField()
