# models.py
from django.db import models

class Webtoon(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()

    def __str__(self):
        return self.title

class Character(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=100)
    description = models.TextField()
    webtoon = models.ForeignKey(Webtoon, related_name='characters', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
