class AbstractBankAccount:
    def __init__(self, account_id, balance):
        self._account_id = account_id
        self._balance = balance

    #get_balance(): float
    def get_balance(self):
        return self._balance

    #deposit(amount: float)
    def deposit(self, amount):
        self._balance += amount

    #withdraw(amount: float):
    def withdraw(self, amount):
        self._balance -= amount

    #account_summary(): str
    def account_summary(self):
        return f"Account ID: {self._account_id}\nBalance: ${self._balance}"

    

