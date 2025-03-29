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
        for row in reader:
            print("\t".join(row))