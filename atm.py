import json
import os
from account import Account

class ATM:
    def __init__(self, data_file="data/accounts.json"):
        self.data_file = data_file
        self.accounts = {}
        self.current_account = None
        self.load_accounts()

    def load_accounts(self):
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    for acc_num, acc_data in data.items():
                        self.accounts[acc_num] = Account.from_dict(acc_data)
        except Exception as e:
            print(f"failed to load accounts: {e}")

    def save_accounts(self):
        try:
            data = {acc_num: acc.to_dict() for acc_num, acc in self.accounts.items()}
            os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            print(f"Failed to save accounts: {e}")

    def create_account(self, account_number: str, pin: str, initial_deposit: float = 0.0):
        if account_number in self.accounts:
            raise ValueError("Account number already exists.")
        if len(pin) != 4 or not pin.isdigit():
            raise ValueError("PIN must be 4 digits.")
        if initial_deposit < 0:
            raise ValueError("Initial deposit cannot be negative.")

        account = Account(account_number, pin, initial_deposit)
        self.accounts[account_number] = account
        self.save_accounts()
        print(f"Account {account_number} created successfully!")

    def authenticate(self, account_number: str, pin: str) -> bool:
        account = self.accounts.get(account_number)
        if account and account.pin == pin:
            self.current_account = account
            return True
        return False

    def check_balance(self):
        return self.current_account.balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.current_account.deposit(amount)
        self.save_accounts()

    def withdraw(self, amount: float):
        self.current_account.withdraw(amount)
        self.save_accounts()

    def show_transaction_history(self):
        return self.current_account.get_transaction_history()

    def logout(self):
        self.current_account = None