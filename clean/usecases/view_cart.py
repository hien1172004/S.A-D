class ViewCartUseCase:
    def __init__(self, cart_repo):
        self.cart_repo = cart_repo

    def execute(self, customer_id):
        return self.cart_repo.get_cart(customer_id)
