import csv
import os
from datetime import datetime
from categories import get_category

DATA_FILE = "data/transactions.csv"

def ensure_file_exists():
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Description", "Amount", "Category"])

def add_transaction():
    ensure_file_exists()
    date = input("Date (YYYY-MM-DD) [leave blank for today]: ") or datetime.today().strftime('%Y-%m-%d')
    description = input("Description: ")
    amount = input("Amount (use - for expenses, + for income): ")
    category = get_category()

    with open(DATA_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([date, description, amount, category])
    print("Transaction added!")

def view_transactions():
    ensure_file_exists()
    with open(DATA_FILE, newline='') as f:
        reader = csv.reader(f)
        rows = list(reader)
        if len(rows) <= 1:
            print("No transactions yet.")
            return

        print(f"{'Date':<12} {'Description':<25} {'Amount':>10} {'Category':<15}")
        print("-" * 65)
        for row in rows[1:]:
            date, desc, amount, category = row
            print(f"{date:<12} {desc:<25} {amount:>10} {category:<15}")
            
def show_summary():
    income, expense = 0, 0
    ensure_file_exists()
    with open(DATA_FILE, newline='') as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            amount = float(row[2])
            if amount > 0:
                income += amount
            else:
                expense += amount

    print("\n=== Summary ===")
    print(f"Total Income:  £{income:.2f}")
    print(f"Total Expense: £{abs(expense):.2f}")
    print(f"Net Balance:   £{income + expense:.2f}")