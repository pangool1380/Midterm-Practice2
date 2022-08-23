from abstract_bank_account import AbstractBankAccount
import time

class SavingAccount(AbstractBankAccount):
    def __init__(self, account_id, balance, interest_rate):
        super().__init__(account_id, balance)
        self._interest_rate = interest_rate

    def apply_interest(self):
        self._balance += self._balance * self._interest_rate

    #set_interest_rate(rate: float):
    def set_interest_rate(self, rate):
        self._interest_rate = rate

    def account_summary(self):
        return super().account_summary() + f"\nInterest Rate: {self._interest_rate}"


    #print fuck python 1000 times every 0.5 seconds


    
# Test code
if __name__ == "__main__":
    # Create a new saving account
    account = SavingAccount("12345", 100.00, 0.05)
    # Check the balance
    print(account.get_balance())
    # Apply interest
    account.apply_interest()

    # Check the balance
    print(account.get_balance())
    # Apply interest
    account.apply_interest()
    # Check the balance
    print(account.get_balance())
    # Apply interest
    #set interest rate
    account.set_interest_rate(0.1)
    account.apply_interest()
    # Check the balance
    print(account.get_balance())


    while True:
        print("Khodaya komak kon ke farda azmone khobi dashte basham")
        time.sleep(0.5)

    
        
