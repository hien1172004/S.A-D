class ViewBooksUseCase:
    def __init__(self, book_repo):
        self.book_repo = book_repo

    def execute(self):
        return self.book_repo.get_all()
