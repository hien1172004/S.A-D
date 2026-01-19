class AddToCartUseCase:
    def __init__(self, cart_repo):
        self.cart_repo = cart_repo

    def execute(self, customer_id, book_id, quantity):
        return self.cart_repo.add_item(customer_id, book_id, quantity)
