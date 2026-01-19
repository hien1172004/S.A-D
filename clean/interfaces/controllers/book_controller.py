from usecases.view_books import ViewBooksUseCase
from infrastructure.repositories.book_repository import DjangoBookRepository

class BookController:
    def list_books(self):
        uc = ViewBooksUseCase(DjangoBookRepository())
        return uc.execute()
