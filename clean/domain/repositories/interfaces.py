class CustomerRepositoryInterface:
    def create(self, name, email, password): pass
    def authenticate(self, email, password): pass

class BookRepositoryInterface:
    def get_all(self): pass

class CartRepositoryInterface:
    def add(self, customer_id, book_id): pass
