from django.db import models
from accounts.models import CustomerModel
from books.models import BookModel

class CartModel(models.Model):
    customer = models.OneToOneField(CustomerModel, on_delete=models.CASCADE)

class CartItemModel(models.Model):
    cart = models.ForeignKey(CartModel, on_delete=models.CASCADE)
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE)
    quantity = models.IntegerField()
