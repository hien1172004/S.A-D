from django.urls import path
from .views import book_detail, list_books

urlpatterns = [
    path('', list_books),
    path('<int:id>/', book_detail),
]
