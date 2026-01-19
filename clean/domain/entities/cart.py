class Cart:
    def __init__(self, id, customer_id):
        self.id = id
        self.customer_id = customer_id
        self.items = []

    def add_item(self, item):
        self.items.append(item)
