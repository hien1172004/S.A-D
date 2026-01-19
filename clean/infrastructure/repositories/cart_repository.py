from cart.models import CartModel, CartItemModel
from books.models import BookModel
from domain.entities.cart import Cart
from domain.entities.cart_item import CartItem

class DjangoCartRepository:

    def add_item(self, customer_id, book_id, quantity):
        cart, _ = CartModel.objects.get_or_create(
            customer_id=customer_id
        )

        book = BookModel.objects.get(id=book_id)

        item, created = CartItemModel.objects.get_or_create(
            cart=cart,
            book=book,
            defaults={"quantity": quantity}
        )

        if not created:
            item.quantity += quantity
            item.save()

        return cart.id
    
    def get_cart(self, customer_id):
        cart_model = CartModel.objects.get(customer_id=customer_id)

        items = []
        for item in CartItemModel.objects.select_related("book").filter(cart=cart_model):
            items.append(
                CartItem(
                    book_id=item.book.id,
                    title=item.book.title,
                    price=item.book.price,
                    quantity=item.quantity
                )
            )
        cart = Cart(
            id=cart_model.id,
            customer_id=customer_id
        )

        for i in items:
            cart.add_item(i)

        return cart
    
    