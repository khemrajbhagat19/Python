class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance

    def calculate_interest(self):
        return self.balance*0.01

    def display(self):
        print(f"Account Number: {self.account_number}, Balance: {self.balance}")

class SavingsAcoount(BankAccount):
    def calculate_interest(self):
        return self.balance * 0.04

class CurrentAcoount(SavingsAcoount):
    def calculate_interest(self):
        return self.balance * 0.02

saccount=SavingsAcoount("5123",1000)
caccount=CurrentAcoount("C456",2000)

saccount.display()
caccount.display()

print(f"Savings Account Interest: {saccount.calculate_interest()}")
print(f"Current Account Interest: {caccount.calculate_interest()}")