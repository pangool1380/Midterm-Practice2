from abstract_bank_account import AbstractBankAccount


class ChequingAccount(AbstractBankAccount):
    def __init__(self, account_id, balance, overdraft_enabled, overdraft_amount):
        super().__init__(account_id, balance)
        #overdraft_enabled: bool
        self._overdraft_enabled = overdraft_enabled
        #overdraft_amount: float
        self._overdraft_amount = overdraft_amount


    #withdraw(amount: float):)
    def withdraw(self, amount):
        if self._overdraft_enabled:
            if self._balance - amount >= self._overdraft_amount:
                self._balance -= amount
            else:
                raise ValueError("Insufficient funds")

        else:
            if self._balance - amount >= 0:
                self._balance -= amount
            else:
                raise ValueError("Insufficient funds")


    #set_overdraft(enabled: bool)
    def set_overdraft(self, enabled):
        if enabled:
            self._overdraft_enabled = True
        else:
            self._overdraft_enabled = False 

    #set_overdraft_amount(amount: float)
    def set_overdraft_amount(self, amount):
        self._overdraft_amount = amount
        if self._overdraft_amount < 0:
            raise ValueError("Overdraft amount cannot be negative")

    #account_summary(): str
    def account_summary(self):
        return super().account_summary() + f"\nOverdraft: {self._overdraft_enabled}\nOverdraft Amount: ${self._overdraft_amount}"


    




# Test code
if __name__ == "__main__":
    # Create a new chequing account
    account = ChequingAccount("12345", 100.00, True, -50.00)
    a2 = ChequingAccount("12345", 100.00, False, 0.00)
    a3 = ChequingAccount("12345", 150.00, True, 0.00)
    # Check the balance
    print(account.get_balance())
    # Withdraw some money
    account.withdraw(50.00)
    # Check the balance
    a2.withdraw(50.00)
    print(a2.get_balance())
    # Withdraw some money
    account.withdraw(150.00)
    # Check the balance
    print(a3.get_balance())




 
   

         