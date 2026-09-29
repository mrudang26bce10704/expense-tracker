# Project Report — Expense Tracker

## 1. Project Title

**Expense Tracker — Command-Line Personal Expense and Budget Management System**

## 2. Introduction

The Expense Tracker is a Python-based command-line application designed to help users record and manage their daily expenses. The system provides basic expense management operations along with spending summaries and monthly budget monitoring.

The project demonstrates fundamental Python programming concepts such as variables, lists, dictionaries, functions, loops, conditional statements, exception handling, and date/time processing.

## 3. Problem Statement

Keeping track of individual expenses manually can make it difficult to determine total spending and monitor a monthly budget. The objective of this project is to develop a simple command-line application that allows a user to maintain expense records and obtain basic spending information.

## 4. Objectives

The main objectives are:

1. Add and store expense records.
2. Assign a unique ID and date to each expense.
3. View all recorded expenses.
4. Update existing expense information.
5. Delete unwanted expense records.
6. Calculate total spending.
7. Generate a monthly spending summary.
8. Set a monthly budget.
9. Compare current-month spending against the configured budget.
10. Provide a fully command-line executable application.

## 5. Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Application development |
| `datetime` | Recording dates and processing monthly summaries |
| Lists | Storing expense records during execution |
| Dictionaries | Representing individual expenses and monthly budgets |
| CLI / Terminal | User interaction |

No external Python packages are required.

## 6. System Features

### 6.1 Add Expense

The user enters a description, amount, and category. The program automatically generates an ID and records the current date.

### 6.2 View Expenses

All recorded expenses are displayed with their ID, date, description, category, and amount.

### 6.3 Update Expense

An expense can be modified by entering its unique ID.

### 6.4 Delete Expense

An expense can be removed using its unique ID.

### 6.5 Total Summary

The system calculates the total amount spent and the total number of recorded expenses.

### 6.6 Monthly Summary

The user selects a month from 1 to 12. The application calculates the total amount and number of expenses for that month in the current year.

### 6.7 Monthly Budget

The user can assign a budget to a particular month.

### 6.8 Budget Check

The application compares spending in the current month with the current month's budget and displays either the remaining amount or a budget-exceeded warning.

## 7. Program Flow

```text
Start
  |
  v
Display Main Menu
  |
  +--> Add Expense
  |
  +--> Update Expense
  |
  +--> Delete Expense
  |
  +--> View Expenses
  |
  +--> View Total Summary
  |
  +--> View Monthly Summary
  |
  +--> Set Monthly Budget
  |
  +--> Check Budget
  |
  +--> Exit
  |
  v
End
```

## 8. Data Structures

Each expense is stored as a dictionary with the following fields:

```text
id
description
amount
category
date
```

All expense dictionaries are stored in the `expenses` list.

Monthly budgets are stored in the `budgets` dictionary using a `(year, month)` tuple as the key.

## 9. Error Handling

The program uses `try-except` blocks to handle invalid numeric input. It also validates month numbers, prevents negative expense/budget values, checks for empty descriptions and categories, and reports when an entered expense ID does not exist.

## 10. Execution Instructions

From the project root, run:

```bash
python main.py
```

If the system uses `python3` instead:

```bash
python3 main.py
```

The program can be operated entirely through the terminal.

## 11. Testing

The following functional cases should be tested before submission:

| Test Case | Expected Result |
|---|---|
| Add valid expense | Expense is added with an ID and date |
| Add negative amount | Input is rejected |
| View expenses with no records | "No expenses found" is displayed |
| Update existing ID | Expense details are updated |
| Update invalid ID | ID-not-found message is displayed |
| Delete existing ID | Expense is removed |
| Delete invalid ID | ID-not-found message is displayed |
| Monthly summary with valid month | Monthly total and count are displayed |
| Monthly summary with invalid month | Invalid-month message is displayed |
| Set valid budget | Budget is saved |
| Check budget below limit | Remaining budget is displayed |
| Check budget above limit | Warning is displayed |
| Exit | Program terminates |

## 12. Limitations

- Data is stored only in memory.
- Closing the program removes all current expense and budget records.
- The monthly summary works for the current year.
- There is no user authentication.
- There is no graphical user interface.
- There is no database integration.

## 13. Future Enhancements

Possible future improvements include:

- Persistent storage using CSV, JSON, SQLite, or another database.
- Expense search and filtering.
- Category-wise spending reports.
- Yearly reports.
- Graphs and charts.
- Exporting reports to CSV or PDF.
- User authentication.
- A graphical or web-based interface.

## 14. Conclusion

The Expense Tracker provides a simple command-line solution for recording expenses and monitoring monthly budgets. The project demonstrates practical use of core Python programming concepts and is executable directly from a terminal without third-party dependencies.

## 15. Repository

Add the final public GitHub repository URL here:

`https://github.com/<github-username>/<repo-name>`
