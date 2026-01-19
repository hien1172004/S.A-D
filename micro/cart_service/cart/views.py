from django.shortcuts import render

# Create your views here.
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cart, CartItem

BOOK_SERVICE = "http://localhost:8002/api/books"

@api_view(['POST'])
def add_to_cart(request):
    cart, _ = Cart.objects.get_or_create(
        customer_id=request.data['customer_id']
    )
    CartItem.objects.create(
        cart=cart,
        book_id=request.data['book_id'],
        quantity=request.data['quantity']
    )
    return Response({"message": "Added"})

@api_view(['GET'])
def view_cart(request, customer_id):
    cart = Cart.objects.get(customer_id=customer_id)
    items = CartItem.objects.filter(cart=cart)

    result = []
    for i in items:
        book = requests.get(f"{BOOK_SERVICE}/{i.book_id}/").json()
        result.append({
            "title": book["title"],
            "price": book["price"],
            "quantity": i.quantity
        })

    return Response(result)
