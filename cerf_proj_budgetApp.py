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
        
        if self.check_funds(amount): 
            self.ledger.append({
            'amount': -amount,
            'description': description
            })
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for transaction in self.ledger:
          balance += transaction['amount']
        return balance
    
    def transfer(self, amount, destination):
        if self.withdraw(amount, f'Transfer to {destination.name}'):
            destination.deposit(amount, f'Transfer from {self.name}')
            return True
        else:
            return False
        
    def check_funds(self, amount):
        return self.get_balance() >= amount

    def __str__(self):
        result = f'{self.name.center(30, "*")}\n'

        for display in self.ledger:
            result += f'{display["description"][:23]:<23}{display["amount"]:>7.2f}\n'

        result += f'Total: {self.get_balance():.2f}'
        return result
        

def create_spend_chart(categories):
    total_spent = 0
    percentages = []

    for category in categories:
        for transaction in category.ledger:
            if transaction['amount'] < 0:
                total_spent += abs(transaction['amount'])

    for category in categories:
        category_spent = 0

        for transaction in category.ledger:
            if transaction['amount'] < 0:
                category_spent += abs(transaction['amount'])

        percentages.append((category_spent / total_spent * 100) // 10 * 10)

    longest_category = max(categories, key=lambda category: len(category.name))

    result = 'Percentage spent by category\n'

    # Bars
    for num in range(100, -10, -10):
        row = f'{num:>3}|'

        for percentage in percentages:
            if percentage >= num:
                row += ' o '
            else:
                row += '   '

        row += '  '
        result += row + '\n'

    # Horizontal line
    result += '    ' + '-' * (3 * len(categories) + 2) + '\n'

    # Vertical category names
    for j in range(len(longest_category.name)):
        row = '     '

        for category in categories:
            if j < len(category.name):
                row += category.name[j] + '  '
            else:
                row += '   '

        result += row

        if j < len(longest_category.name) - 1:
            result += '\n'

    return result





