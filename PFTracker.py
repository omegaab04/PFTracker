from transactions import add_transaction, view_transactions
from utils import clear_screen

def main_menu():
    while True:
        clear_screen()
        print("=== Personal Finance Tracker ===")
        print("1. Add a transaction")
        print("2. View all transactions")
        print("3. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_transactions()
            input("\nPress Enter to return to the menu...")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main_menu()