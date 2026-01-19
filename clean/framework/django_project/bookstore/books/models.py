from django.db import models

class BookModel(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
