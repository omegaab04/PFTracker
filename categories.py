def get_category():
    categories = ["Food", "Transport", "Utilities", "Entertainment", "Health", "Salary", "Other"]
    print("Select a category:")
    for i, cat in enumerate(categories, 1):
        print(f"{i}. {cat}")
    while True:
        try:
            choice = int(input("Enter number: "))
            if 1 <= choice <= len(categories):
                return categories[choice - 1]
        except ValueError:
            pass
        print("Invalid input, try again.")