from django.urls import path
from .views import add_to_cart, view_cart, view_cart_page, add_to_cart_page

urlpatterns = [
    path("add/", add_to_cart),
    path("api/", view_cart),
    path("", view_cart_page),
    path("add/<int:book_id>/", add_to_cart_page),
    
]
