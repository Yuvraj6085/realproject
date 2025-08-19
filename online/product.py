class Product:
    def __init__(self, product_id: str, name: str, price: float, stock: int):
        self.product_id = product_id
        self.name = name.strip().title()
        self.price = self._validate_price(price)
        self.stock = self._validate_stock(stock)

    def _validate_price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        return round(float(price), 2)

    def _validate_stock(self, stock):
        if stock < 0:
            raise ValueError("Stock cannot be negative.")
        return int(stock)

    def reduce_stock(self, quantity: int):
        if quantity > self.stock:
            raise ValueError(f"Only {self.stock} in stock.")
        self.stock -= quantity

    def restock(self, quantity: int):
        self.stock += quantity

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "stock": self.stock
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            product_id=data["product_id"],
            name=data["name"],
            price=data["price"],
            stock=data["stock"]
        )

    def __str__(self):
        return f"[{self.product_id}] {self.name} - ₹{self.price:.2f} ({self.stock} in stock)"