
from datetime import datetime

expenses = []
budgets = {}

next_id = 1


def add_expense():
    desc = input("Enter description: ")
    amount = float(input("Enter amount: ₹"))
    cat = input("Enter category: ")

    global next_id

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
        print(f"{e['id']} | {e['date']} | {e['description']} | {e['category']} | ₹{e['amount']:.2f}")

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


def total_summary():
    total = 0
    for e in expenses:
        total += e["amount"]

    print("\n----- Expense Summary -----")
    print(f"Total spent: ₹{total:.2f}")
    print(f"Total expenses: {len(expenses)}\n")


def monthly_summary():
    try:
        month = int(input("Enter month number (1-12): "))
        if month < 1 or month > 12:
            print("Invalid month number.\n")
            return

        year = datetime.now().year
        total = 0
        count = 0

        for e in expenses:
            d = datetime.strptime(e["date"], "%Y-%m-%d")
            if d.year == year and d.month == month:
                total += e["amount"]
                count += 1

        print(f"\n----- Summary for {month}/{year} -----")
        print(f"Total spent: ₹{total:.2f}")
        print(f"Number of expenses: {count}\n")

    except ValueError:
        print("Please enter a valid month number.\n")


def set_budget():
    try:
        month = int(input("Enter month number (1-12): "))
        budget = float(input("Enter budget: ₹"))

        if month < 1 or month > 12:
            print("Invalid month.\n")
            return

        year = datetime.now().year
        budgets[(year, month)] = budget
        print("Budget saved!\n")

    except ValueError:
        print("Please enter valid numbers.\n")


def check_budget():
    now = datetime.now()
    year = now.year
    month = now.month

    key = (year, month)

    # calculate spent
    spent = 0
    for e in expenses:
        d = datetime.strptime(e["date"], "%Y-%m-%d")
        if d.year == year and d.month == month:
            spent += e["amount"]

    if key not in budgets:
        print("No budget set for this month.\n")
        return

    budget = budgets[key]
    print("\n----- Budget Check -----")
    print(f"Budget: ₹{budget:.2f}")
    print(f"Spent: ₹{spent:.2f}")

    

    if spent > budget:
        print("WARNING: You exceeded your budget!\n")
    else:
        print(f"Remaining: ₹{budget - spent:.2f}\n")


while True:
    print("========== EXPENSE TRACKER ==========")

    
    print("1. Add Expense")
    print("2. Update Expense")
    print("3. Delete Expense")
    print("4. View All Expenses")
    print("5. View Total Summary")
    print("6. View Monthly Summary")
    
    print("7. Set Monthly Budget")
    print("8. Check Budget")
    print("9.. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_expense()
    elif choice == "2":
        update_expense()
    elif choice == "3":
        delete_expense()
    elif choice == "4":
        view_expenses()
    elif choice == "5":
        total_summary()
    elif choice == "6":
        monthly_summary()
    elif choice == "7":

        
        set_budget()
    elif choice == "8":
        check_budget()
    elif choice == "9":
        print("Thanks for using Expense Tracker!")
        break
    else:
        print("Invalid choice. Try again.\n")
