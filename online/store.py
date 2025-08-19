# store.py
import json
import os
from user import User
from product import Product
from cart import ShoppingCart
from order import Order

class Store:
    def __init__(self):
        self.users = {}
        self.products = {}
        self.orders = {}
        self.current_user = None
        self.cart = ShoppingCart()
        self.data_files = {
            "users": "data/users.json",
            "products": "data/products.json",
            "orders": "data/orders.json"
        }
        self.load_all_data()

    def load_all_data(self):
        self._load_data("users", User)
        self._load_data("products", Product)
        self._load_data("orders", Order)

    def _load_data(self, entity: str, cls):
        path = self.data_files[entity]
        try:
            if os.path.exists(path):
                with open(path, 'r') as f:
                    data = json.load(f)
                    for key, value in data.items():
                        self.__dict__[entity][key] = cls.from_dict(value)
        except Exception as e:
            print(f"  Failed to load {entity}: {e}")

    def save_all_data(self):
        self._save_data("users", {u: user.to_dict() for u, user in self.users.items()})
        self._save_data("products", {p: prod.to_dict() for p, prod in self.products.items()})
        self._save_data("orders", {o: order.to_dict() for o, order in self.orders.items()})

    def _save_data(self, entity: str, data: dict):
        try:
            path = self.data_files[entity]
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'w') as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            print(f" Failed to save {entity}: {e}")

    def register_user(self, username: str, password: str, email: str):
        if username in self.users:
            raise ValueError("Username already exists.")
        user = User(username, password, email)
        self.users[username] = user
        self.save_all_data()
        print(f" Registered successfully: {username}")

    def login(self, username: str, password: str) -> bool:
        user = self.users.get(username)
        if user and user.password == password:
            self.current_user = user
            self.cart = ShoppingCart()  # Fresh cart
            print(f" Logged in as {username}")
            return True
        print(" Invalid username or password.")
        return False

    def logout(self):
        if self.current_user:
            print(f" Logged out {self.current_user.username}")
            self.current_user = None
            self.cart.clear()

    def browse_products(self):
        if not self.products:
            print(" No products available.")
            return
        print("\n AVAILABLE PRODUCTS:")
        print("-" * 60)
        for product in self.products.values():
            print(product)
        print("-" * 60)

    def add_to_cart(self, product_id: str, quantity: int = 1):
        product = self.products.get(product_id)
        if not product:
            raise ValueError("Product not found.")
        if quantity > product.stock:
            raise ValueError(f"Only {product.stock} available.")
        self.cart.add_item(product_id, quantity)
        print(f"Added {quantity}x {product.name} to cart.")

    def view_cart(self):
        if self.cart.is_empty():
            print(" Your cart is empty.")
            return
        print("\n YOUR CART:")
        print("-" * 60)
        total = 0.0
        for pid, qty in self.cart.get_items_with_quantity().items():
            product = self.products[pid]
            item_total = product.price * qty
            total += item_total
            print(f"{product.name} x{qty} = ₹{item_total:.2f}")
        print("-" * 60)
        print(f" TOTAL: ₹{total:.2f}")

    def place_order(self):
        if self.cart.is_empty():
            raise ValueError("Cannot place empty order.")

        total = 0.0
        order_items = {}

        for pid, qty in self.cart.get_items_with_quantity().items():
            product = self.products[pid]
            if qty > product.stock:
                raise ValueError(f"Not enough stock for {product.name}.")
            total += product.price * qty
            order_items[pid] = qty

        # Deduct stock
        for pid, qty in order_items.items():
            self.products[pid].reduce_stock(qty)

        # Create order
        order = Order(self.current_user.username, order_items, total)
        self.orders[order.order_id] = order

        # Clear cart
        self.cart.clear()

        self.save_all_data()
        print(f"Order {order.order_id} placed successfully! Total: ₹{total:.2f}")