from datetime import datetime

expenses = []
next_id = 1


def add_expense():
    global next_id

    desc = input("Enter description: ")
    amount = float(input("Enter amount: ₹"))
    cat = input("Enter category: ")

    expenses.append({
        "id": next_id,
        "description": desc,
        "amount": amount,
        "category": cat,
        "date": datetime.now().strftime("%Y-%m-%d")
    })

    next_id += 1
    print("Expense added!\n")


def view_expenses():
    if not expenses:
        print("No expenses found.\n")
        return

    print("\nID | Date | Description | Category | Amount")
    print("-" * 70)

    for e in expenses:
        print(
            f"{e['id']} | {e['date']} | "
            f"{e['description']} | {e['category']} | "
            f"₹{e['amount']:.2f}"
        )

    print()


def update_expense():
    view_expenses()

    if not expenses:
        return

    try:
        exp_id = int(input("Enter expense ID to update: "))

        for e in expenses:
            if e["id"] == exp_id:
                e["description"] = input("New description: ")
                e["amount"] = float(input("New amount: ₹"))
                e["category"] = input("New category: ")

                print("Updated successfully!\n")
                return

        print("Expense ID not found.\n")

    except ValueError:
        print("Please enter a valid number.\n")


def delete_expense():
    view_expenses()

    if not expenses:
        return

    try:
        exp_id = int(input("Enter expense ID to delete: "))

        for e in expenses:
            if e["id"] == exp_id:
                expenses.remove(e)
                print("Deleted successfully!\n")
                return

        print("Expense ID not found.\n")

    except ValueError:
        print("Please enter a valid number.\n")
