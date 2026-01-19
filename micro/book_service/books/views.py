from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book

@api_view(['GET'])
def list_books(request):
    return Response([
        {
            "id": b.id,
            "title": b.title,
            "price": b.price
        } for b in Book.objects.all()
    ])

@api_view(['GET'])
def book_detail(request, id):
    b = Book.objects.get(id=id)
    return Response({
        "id": b.id,
        "title": b.title,
        "price": b.price
    })
