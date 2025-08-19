import json 
from datetime import datetime
class Account:
    def __init__(self,acc_number:str,pin:str,balance: float=0.0):
        self.acc_number = acc_number
        self.pin = pin
        self.balance = balance
        self.transaction=[]
    def deposite(self,amount: float):
        self.balance+=amount
        self.add_transaction("deposite",amount)
    def withdraw(self,amount: float):
        if amount>self.balance:
            raise ValueError("Insufficient balance")
        self.balance-=amount
        self.add_transaction("withdraw",amount)
    def add_transaction(self,action:str,amount: float):
        transaction={
            "action":action,
            "amount":amount,
            "balance_after":self.balance,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        }
        self.transactions.append(transaction)
    def get_transactions_history(self):
        return self.transactions.copy()
    def to_dict(self):
        return {
            "account_number": self.account_number,
            "pin": self.pin,
            "balance": self.balance,
            "transactions": self.transactions
        }
    @classmethod
    def from_dict(cls, data):
        account = cls(data["account_number"], data["pin"], data["balance"])
        account.transactions = data["transactions"]
        return account