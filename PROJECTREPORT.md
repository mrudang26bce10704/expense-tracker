# Project Report — Expense Tracker

## 1. Project Title

**Expense Tracker – Command-Line Personal Expense and Budget Management System**

## 2. Introduction

The Expense Tracker is a Python-based command-line application used to manage daily expenses. It allows users to add, view, update, and delete expenses. It also provides total and monthly spending summaries and allows users to set and check monthly budgets.

The project is organized into separate Python modules so that different parts of the application are easier to understand, maintain, and reuse. `main.py` controls the menu and calls functions from the other modules.

This project uses basic Python concepts such as functions, modules, lists, dictionaries, loops, conditional statements, exception handling, imports, and the `datetime` module.

## 3. Problem Statement

Managing daily expenses manually can make it difficult to keep track of total spending and monthly budgets. This project provides a simple command-line solution for recording expenses and monitoring monthly spending.

## 4. Objectives

* Add, update, view, and delete expenses.
* Automatically assign an ID and date to each expense.
* Calculate total and monthly spending.
* Set a monthly budget.
* Check spending against the current month's budget.
* Divide the program into separate Python modules.
* Create a simple command-line application using Python.

## 5. Technologies Used

| Technology | Purpose |
| ---------- | ------- |
| Python 3 | Application development |
| `datetime` | Date handling |
| Lists & Dictionaries | Data storage |
| Python Modules | Separating program functionality |
| Command Line | User interaction |

No external Python packages are required.

## 6. Project Structure

```text
expense-tracker/
│
├── main.py
├── expense.py
├── summary.py
├── budget.py
├── README.md
├── PROJECT_REPORT.md
├── requirements.txt
└── .gitignore
```

### Module Description

* **`main.py`** — Contains the main menu and controls the program by calling functions from the other modules.
* **`expense.py`** — Contains functions for adding, viewing, updating, and deleting expenses. It also stores the `expenses` list.
* **`summary.py`** — Contains functions for calculating total and monthly expense summaries.
* **`budget.py`** — Contains functions for setting and checking monthly budgets.

The modules are connected using Python `import` statements. For example, `main.py` imports the required functions from `expense.py`, `summary.py`, and `budget.py`.

## 7. Main Features

### Add Expense

Users can enter the description, amount, and category of an expense. The program automatically records the date and assigns an ID.

### View, Update and Delete

Users can view all expenses and modify or delete an expense using its ID.

### Expense Summary

The program displays the total amount spent and the total number of expenses.

### Monthly Summary

Users can select a month to view the total spending and number of expenses for that month.

### Budget Management

Users can set a monthly budget and check whether their current spending is within the budget.

## 8. Program Flow

```text
Start
  ↓
main.py
  ↓
Display Menu
  ↓
Add / Update / Delete / View Expenses
  ↓
View Summaries / Set Budget / Check Budget
  ↓
Exit
  ↓
End
```

## 9. Module Flow

```text
                    main.py
                       |
          +------------+------------+
          |            |            |
          ↓            ↓            ↓
      expense.py   summary.py   budget.py
          |            |            |
          +------------+------------+
                       |
                Shared expense data
```

`main.py` acts as the controller. It imports and calls the functions required for each menu option.

## 10. Data Structures

Each expense is stored as a dictionary containing:

```text
id, description, amount, category, date
```

These dictionaries are stored in the `expenses` list. Monthly budgets are stored in the `budgets` dictionary using the year and month as the key.

## 11. Error Handling

The program handles invalid inputs such as:

* Invalid numbers or expense IDs
* Invalid month numbers
* Invalid amount or budget input
* Non-existing expense IDs

## 12. Execution

Make sure all Python modules are in the same project folder:

```text
expense-tracker/
├── main.py
├── expense.py
├── summary.py
└── budget.py
```

From the project folder, run:

```bash
python main.py
```

or:

```bash
python3 main.py
```

Python automatically imports the required modules when `main.py` is executed. The individual module files do not need to be compiled or run separately.

The application can be completely operated through the terminal.

## 13. Testing

The main functions were tested for adding, updating, deleting, and viewing expenses, generating monthly summaries, setting budgets, and checking budget limits. Invalid inputs were also tested to ensure that the program displays suitable error messages.

## 14. Limitations

* Data is stored only while the program is running.
* Data is lost when the program is closed.
* There is no database or graphical interface.
* The monthly summary is based on the current year.
* The application uses separate modules but does not yet use permanent file or database storage.

## 15. Future Enhancements

Future versions could include database storage, expense searching and filtering, category-wise reports, graphs, CSV/PDF export, user authentication, and a graphical or web interface.

## 16. Conclusion

The Expense Tracker provides a simple way to manage daily expenses and monthly budgets through the command line. Separating the program into modules makes the code easier to organize, maintain, and understand. The project demonstrates the practical use of fundamental Python programming concepts, including functions, modules, lists, dictionaries, loops, conditionals, exception handling, and imports.

## 17. GitHub Repository

**Repository:**

https://github.com/mrudang26bce10704/expense-tracker
