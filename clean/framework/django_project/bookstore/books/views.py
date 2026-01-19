from django.http import JsonResponse
from interfaces.controllers.book_controller import BookController

controller = BookController()

def list_books(request):
    books = controller.list_books()
    return JsonResponse([
        {
            "id": b.id,
            "title": b.title,
            "author": b.author,
            "price": b.price,
            "stock": b.stock
        } for b in books
    ], safe=False)
from django.shortcuts import render

def list_books_page(request):
    books = controller.list_books()
    return render(
        request,
        "books/list.html",
        {"books": books}
    )
