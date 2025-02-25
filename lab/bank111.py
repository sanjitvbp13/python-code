#A program that models a bank account, with classes for the account, the customer, and the bank.
class Bank:
    def __init__(self,initial_amount=0):
        self.balance=initial_amount
        print(self.balance)

    def deposit_money(self):
        amount = float(input("Enter the amount to be deposited : "))
        self.balance += amount
        return self.balance

    def withdraw_money(self):
        amount = float(input("Enter the amount to be withdraw : "))
        if amount >= self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return f"Money withdrawn successfuly {amount}"

    def display_money(self):
        print("The current balance:", self.balance)

bank=Bank()
bank.deposit_money()
print(bank.withdraw_money())
bank.display_money()
