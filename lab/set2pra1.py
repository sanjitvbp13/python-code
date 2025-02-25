class bank:
    def __init__(self, initial_amount):
        initial_amount = 0

    def deposite_money(self):
        amount = float(input("enter the amount to  be deposited : "))
        self.initial_amount += amount

    def  withdraw_money(self, amount):
        if  amount <= self.initial_amount:
            self.initial_amount -= amount
            return "Money withdrawn"
        else:
            return "not efficent money"
 
    def display_money(self, amount):
        print("The final amount : ", self.initial_amount + amount)

