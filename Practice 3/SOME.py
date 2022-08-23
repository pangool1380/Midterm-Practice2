#Create a abstract class
from abstract_bank_account import AbstractBankAccount

class AbstractBankAccount:
    def show_details(self):
        raise NotImplementedError("Subclass must implement abstract method")
       