# cart.py
class ShoppingCart:
    def __init__(self):
        self.items = {}  

    def add_item(self, product_id: str, quantity: int = 1):
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        self.items[product_id] = self.items.get(product_id, 0) + quantity

    def remove_item(self, product_id: str):
        self.items.pop(product_id, None)

    def update_quantity(self, product_id: str, quantity: int):
        if quantity <= 0:
            self.remove_item(product_id)
        else:
            if product_id in self.items:
                self.items[product_id] = quantity
            else:
                raise ValueError("Item not in cart.")

    def clear(self):
        self.items.clear()

    def get_items_with_quantity(self):
        return self.items.copy()

    def is_empty(self):
        return len(self.items) == 0