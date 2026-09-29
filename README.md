# Expense Tracker

A simple command-line Expense Tracker made using Python. It helps users add, view, update, and delete expenses. It also provides spending summaries and monthly budget checking.

The application is divided into separate Python modules so that each part of the program has a clear responsibility.

## Features

* Add expenses with description, amount, category, and date
* View all expenses
* Update and delete expenses using their ID
* View total spending
* View monthly spending
* Set a monthly budget
* Check if the monthly budget has been exceeded
* Uses separate Python modules for better organization
* Runs completely through the command line
* Uses only Python's built-in modules

## Project Structure

```text
expense-tracker/
│
├── main.py
├── expense.py
├── summary.py
├── budget.py
├── README.md
├── PROJECTREPORT.md
├── .gitignore
├── requirements.txt
├── statement.md
```

### Python Files

| File | Purpose |
| --- | --- |
| `main.py` | Displays the menu and controls the application |
| `expense.py` | Adds, views, updates, and deletes expenses |
| `summary.py` | Calculates total and monthly expense summaries |
| `budget.py` | Sets and checks monthly budgets |

`main.py` imports the required functions from the other Python files.

## Requirements

* Python 3.8 or later
* Terminal / Command Prompt
* No external packages are needed

## Setup

Clone the repository:

```bash
git clone https://github.com/mrudang26bce10704/expense-tracker.git
```

Open the project folder:

```bash
cd expense-tracker
```

Check Python:

```bash
python --version
```

## Running the Project

Run the main program:

```bash
python main.py
```

If required, use:

```bash
python3 main.py
```

You only need to run `main.py`. Python automatically loads the imported modules (`expense.py`, `summary.py`, and `budget.py`).

The program will show a menu:

```text
========== EXPENSE TRACKER ==========
1. Add Expense
2. Update Expense
3. Delete Expense
4. View All Expenses
5. View Total Summary
6. View Monthly Summary
7. Set Monthly Budget
8. Check Budget
9. Exit
```

Enter the option number to perform the required action.

## How It Works

### Add Expense

Enter the description, amount, and category. The program automatically adds the date and gives the expense a unique ID.

The functionality is implemented in `expense.py`.

### Update / Delete Expense

Enter the expense ID to update or delete an existing expense.

These functions are implemented in `expense.py`.

### Summaries

The program can show total spending and spending for a selected month.

These functions are implemented in `summary.py`.

### Budget

A monthly budget can be set and checked against the current month's spending. If the spending goes above the budget, a warning is displayed.

These functions are implemented in `budget.py`.

### Main Program

`main.py` contains the main menu. It imports functions from the other modules and calls the appropriate function based on the user's choice.

For example:

```python
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
```

## Data Storage

The expenses and budgets are stored in Python lists and dictionaries while the program is running.

**Note:** Data is not permanently saved. All data will be lost when the program is closed.

## Error Handling

The program handles invalid inputs such as:

* Invalid numbers or IDs
* Invalid month numbers
* Invalid amount or budget input
* IDs that do not exist

## Technologies Used

* Python 3
* `datetime`
* Lists and dictionaries
* Python modules
* Command-line interface (CLI)

## Author

**Mrudang Pranav Shah**  
**26BCE10704**  
**Computer Science Engineering Core**
