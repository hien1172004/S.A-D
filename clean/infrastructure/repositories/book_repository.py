from domain.entities.book import Book
from books.models import BookModel

class DjangoBookRepository:
    def get_all(self):
        books = BookModel.objects.all()
        return [
            Book(b.id, b.title, b.author, b.price, b.stock)
            for b in books
        ]
