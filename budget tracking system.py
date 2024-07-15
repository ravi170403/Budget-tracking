import os
from datetime import datetime

class Transaction:
    def __init__(self, category, amount, date):
        self.category = category  # Category of the transaction
        self.amount = amount      # Amount of the transaction
        self.date = date          # Date of the transaction

    def __str__(self):
        # This method returns a string representation of the transaction
        return f"{self.date} | {self.category} | {'-' if self.amount < 0 else ''}${abs(self.amount):.2f}"

class BudgetTracker:
    def __init__(self):
        self.transactions = []  # List to store transactions
        self.load_transactions()

    def add_transaction(self, category, amount):
        date = datetime.now().strftime("%Y-%m-%d")
        self.transactions.append(Transaction(category, amount, date))
        self.save_transactions()

    def calculate_budget(self):
        total_income = sum(t.amount for t in self.transactions if t.amount > 0)
        total_expenses = sum(t.amount for t in self.transactions if t.amount < 0)
        return total_income + total_expenses

    def categorize_expenses(self):
        categories = {}
        for t in self.transactions:
            if t.amount < 0:
                if t.category not in categories:
                    categories[t.category] = 0
                categories[t.category] += t.amount
        return categories

    def save_transactions(self):
        with open('transactions.txt', 'w') as file:
            for t in self.transactions:
                file.write(f"{t.date},{t.category},{t.amount}\n")

    def load_transactions(self):
        if os.path.exists('transactions.txt'):
            with open('transactions.txt', 'r') as file:
                for line in file:
                    date, category, amount = line.strip().split(',')
                    self.transactions.append(Transaction(category, float(amount), date))

def print_menu():
    print("\nBudget Tracker Menu")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Budget")
    print("4. View Expense Analysis")
    print("5. Exit")

def add_income(tracker):
    category = input("Enter income category: ")
    amount = float(input("Enter amount: "))
    tracker.add_transaction(category, amount)
    print("Income added successfully.")

def add_expense(tracker):
    category = input("Enter expense category: ")
    amount = float(input("Enter amount: "))
    tracker.add_transaction(category, -amount)
    print("Expense added successfully.")

def view_budget(tracker):
    budget = tracker.calculate_budget()
    print(f"Remaining Budget: ${budget:.2f}")

def view_expense_analysis(tracker):
    categories = tracker.categorize_expenses()
    print("\nExpense Analysis by Category:")
    for category, amount in categories.items():
        print(f"{category}: ${amount:.2f}")

def main():
    tracker = BudgetTracker()
    while True:
        print_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            add_income(tracker)
        elif choice == '2':
            add_expense(tracker)
        elif choice == '3':
            view_budget(tracker)
        elif choice == '4':
            view_expense_analysis(tracker)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
