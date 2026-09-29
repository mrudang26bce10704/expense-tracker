from datetime import datetime
from expense import expenses


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
