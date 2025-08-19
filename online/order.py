# order.py
from datetime import datetime

class Order:
    def __init__(self, username: str, items: dict, total: float):
        self.order_id = f"ORD-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        self.username = username
        self.items = items  # {product_id: quantity}
        self.total = round(total, 2)
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "order_id": self.order_id,
            "username": self.username,
            "items": self.items,
            "total": self.total,
            "timestamp": self.timestamp
        }

    @classmethod
    def from_dict(cls, data):
        order = cls(data["username"], data["items"], data["total"])
        order.order_id = data["order_id"]
        order.timestamp = data["timestamp"]
        return order