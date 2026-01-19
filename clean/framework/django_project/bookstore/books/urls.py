from django.urls import path
from .views import list_books, list_books_page

urlpatterns = [

     # UI
    path("", list_books_page),
    path("api/", list_books),
]
