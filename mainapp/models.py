from django.db import models


class WordLinks(models.Model):
    word = models.CharField(max_length=50)
    href = models.CharField(max_length=150)