from usecases.add_to_cart import AddToCartUseCase
from usecases.view_cart import ViewCartUseCase
from infrastructure.repositories.cart_repository import DjangoCartRepository

class CartController:
    def __init__(self):
        repo = DjangoCartRepository()
        self.add_uc = AddToCartUseCase(repo)
        self.view_uc = ViewCartUseCase(repo)

    def add(self, data):
        return self.add_uc.execute(
            data["customer_id"],
            data["book_id"],
            data.get("quantity", 1)
        )

    def view(self, customer_id):
        return self.view_uc.execute(customer_id)
