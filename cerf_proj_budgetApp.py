class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({
        'amount': amount,
        'description': description
        })

    def withdraw(self, amount, description=''):
        balance = 0 

        for transaction in self.ledger:
          balance += transaction['amount']
        
        if balance >= amount: 
            self.ledger.append({
            'amount': (-1*amount),
            'description': description
            })
            return True
        else:
            return False


food = Category("Food")

food.deposit(100, "Starting money")

food.withdraw(30, "Lunch")

food.withdraw(80, "Dinner")

print(food.ledger)
