class Category():
    
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0

    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})
        self.balance += amount  # Aktualisiere das Guthaben

    def withdraw (self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            self.balance -= amount  # Aktualisiere das Guthaben nach der Auszahlung
            return True
        return False
    
    def get_balance(self):
        return self.balance  # Gib das aktuelle Guthaben zurück
    
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False 
        
    def check_funds(self, amount):
        return self.balance >= amount  # Überprüft, ob genügend Guthaben vorhanden ist

    def __str__(self):
        title = f"*************{self.name}*************"
        items = "\n".join([f"{item['description'][:23]:<23}{item['amount']:>7.2f}" for item in self.ledger])
        total = f"Total: {self.get_balance():.2f}"
        return f"{title}\n{items}\n{total}"

def create_spend_chart(categories):
    spent = []
    total_spent = 0

    for category in categories:
        total = sum(-item["amount"] for item in category.ledger if item["amount"] < 0)
        spent.append(total)
        total_spent += total

    percentages = [int((amount / total_spent) * 100) // 10 * 10 for amount in spent]

    chart = "Percentage spent by category\n"

    for i in range(100, -1, -10):
        line = str(i).rjust(3) + "|"
        for p in percentages:
            line += " o " if p >= i else "   "
        line += " "  # wichtiges Leerzeichen am Zeilenende
        chart += line + "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_len = max(len(cat.name) for cat in categories)

    for i in range(max_len):
        line = "     "
        for cat in categories:
            if i < len(cat.name):
                line += cat.name[i] + "  "
            else:
                line += "   "
        chart += line + "\n"

    return chart.rstrip("\n")

food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')

clothing = Category('Clothing')
food.transfer(50, clothing)

print(food)
print(clothing)

categories = [food, clothing]
print(create_spend_chart(categories))

