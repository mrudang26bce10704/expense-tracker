from expense import (
    add_expense,
    update_expense,
    delete_expense,
    view_expenses
)

from summary import (
    total_summary,
    monthly_summary
)

from budget import (
    set_budget,
    check_budget
)

def main():
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
        print("9. Exit")

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


if __name__ == "__main__":
    main()
