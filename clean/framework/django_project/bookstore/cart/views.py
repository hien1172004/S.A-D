from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from interfaces.controllers.cart_controller import CartController

controller = CartController()

@csrf_exempt
def add_to_cart(request):
    data = json.loads(request.body)
    cart_id = controller.add(data)
    return JsonResponse({"cart_id": cart_id})
from django.http import JsonResponse

def view_cart(request):
    customer_id = request.GET.get("customer_id")
    cart = controller.view(customer_id)

    return JsonResponse({
        "cart_id": cart.id,
        "items": [
            {
                "book_id": i.book_id,
                "title": i.title,
                "quantity": i.quantity,
                "price": i.price
            }
            for i in cart.items
        ]
    })

from django.shortcuts import render, redirect

def view_cart_page(request):
    if not request.session.get("customer_id"):
        return redirect("/login/")

    cart = controller.view(request.session["customer_id"])

    return render(
        request,
        "cart/cart.html",
        {"cart": cart}
    )

def add_to_cart_page(request, book_id):
    customer_id = request.session.get("customer_id")

    if not customer_id:
        return redirect("/login/")

    controller.add({
        "customer_id": customer_id,
        "book_id": book_id,
        "quantity": 1
    })

    return redirect("/cart/")