# Problem Statement

## Expense Tracker

Managing daily expenses manually can make it difficult to keep track of total spending, expense categories, and monthly budgets. Without a simple system, users may find it difficult to monitor their spending and determine whether they are staying within their planned budget.

The objective of this project is to create a simple command-line **Expense Tracker** using Python.

The program should allow a user to:

1. Add a new expense.
2. View all recorded expenses.
3. Update an existing expense.
4. Delete an existing expense.
5. View the total amount spent and number of expenses.
6. View spending for a selected month.
7. Set a monthly budget.
8. Check the current month's spending against the budget.

Each expense contains:

* An automatically generated ID
* Description
* Amount
* Category
* Automatically generated date

A new expense is automatically assigned a unique ID and the current date when it is added. The user can later update or delete an expense using its ID.

For the monthly summary, the user selects a month number from 1 to 12. The program calculates the total amount spent and the number of expenses recorded for that month in the current year.

For budget management, the user can set a budget for a particular month. The program compares the current month's spending with the stored budget and displays either the remaining budget or a warning when the budget has been exceeded.

The program stores expenses in memory using a list of dictionaries. Monthly budgets are stored in a dictionary using the year and month as the key. No external database or data file is required.

The program is divided into separate Python modules:

* `main.py` — Controls the main menu and program flow.
* `expense.py` — Handles adding, viewing, updating, and deleting expenses.
* `summary.py` — Handles total and monthly expense summaries.
* `budget.py` — Handles setting and checking monthly budgets.

## Objective

The main objective is to build a simple Python-based system that demonstrates how basic programming concepts can be used to manage expenses and monitor monthly spending.

The project demonstrates:

* Variables
* Lists
* Dictionaries
* Functions
* Modules and `import`
* Loops
* Conditional statements
* User input
* Exception handling
* Searching through stored data
* Updating stored data
* Date and time handl
