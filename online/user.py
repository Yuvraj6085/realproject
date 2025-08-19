# user.py
import re

class User:
    def __init__(self, username: str, password: str, email: str):
        self.username = self._validate_username(username)
        self.password = self._validate_password(password)
        self.email = self._validate_email(email)

    def _validate_username(self, username):
        username = username.strip().lower()
        if not re.match(r"^[a-z0-9_]{3,20}$", username):
            raise ValueError("Username: 3-20 chars, lowercase, digits, underscore only.")
        return username

    def _validate_password(self, password):
        if len(password) < 6:
            raise ValueError("Password must be at least 6 characters.")
        return password  # In real app: hash it!

    def _validate_email(self, email):
        email = email.strip().lower()
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email format.")
        return email

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "email": self.email
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            username=data["username"],
            password=data["password"],
            email=data["email"]
        )