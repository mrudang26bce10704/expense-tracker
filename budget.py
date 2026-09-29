from datetime import datetime
from expense import expenses

budgets = {}


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
