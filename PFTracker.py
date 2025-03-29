from transactions import add_transaction, view_transactions, show_summary
from utils import clear_screen, highlight, error, success
from colorama import init

init(autoreset=True)

def main_menu():
    while True:
        clear_screen()
        print(highlight("=== Personal Finance Tracker ==="))
        print("1. Add a transaction")
        print("2. View all transactions")
        print("3. View summary")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            add_transaction()
            input(success("\nTransaction added! Press Enter to return to the menu..."))
        elif choice == '2':
            view_transactions()
            input(highlight("\nPress Enter to return to the menu..."))
        elif choice == '3':
            show_summary()
            input(highlight("\nPress Enter to return to the menu..."))
        elif choice == '4':
            print(success("Goodbye! 👋"))
            break
        else:
            print(error("Invalid option. Try again."))
            input("Press Enter...")

if __name__ == "__main__":
    main_menu()