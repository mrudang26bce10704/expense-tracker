# Expense Tracker

A simple command-line Expense Tracker developed in Python. The application allows users to record, view, update, and delete expenses, generate spending summaries, and manage monthly budgets.

## Features

- Add a new expense with:
  - Description
  - Amount
  - Category
  - Automatically generated date
- View all recorded expenses
- Update an existing expense using its ID
- Delete an expense using its ID
- View total spending and number of expenses
- View spending for a selected month
- Set a monthly budget
- Check the current month's budget status
- Displays a warning when spending exceeds the current monthly budget
- Runs entirely from the command line
- Uses only Python's standard library; no external packages are required

## Project Structure

```text
expense-tracker/
├── main.py
├── README.md
├── PROJECT_REPORT.md
├── requirements.txt
└── .gitignore
```

## Requirements

- Python 3.8 or later
- A terminal/command prompt
- No external Python packages are required

## Installation and Setup

### 1. Clone the repository

Replace the URL below with your public GitHub repository URL:

```bash
git clone https://github.com/<github-username>/<repo-name>.git
```

### 2. Open the project directory

```bash
cd <repo-name>
```

### 3. Verify Python

```bash
python --version
```

On some systems, use:

```bash
python3 --version
```

### 4. Install dependencies

There are no third-party dependencies. The `requirements.txt` file is intentionally empty.

If your environment requires the command, run:

```bash
pip install -r requirements.txt
```

## Running the Project

Run the application from the project root:

```bash
python main.py
```

Or, on systems where Python 3 is invoked with `python3`:

```bash
python3 main.py
```

The program will display a menu similar to:

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
Enter your choice:
```

Enter the number corresponding to the operation you want to perform.

## How to Use

### Add Expense

Select option `1` and enter the description, amount, and category.

Example:

```text
Enter description: Lunch
Enter amount: ₹150
Enter category: Food
```

The application automatically records the current date and assigns a unique expense ID.

### Update Expense

Select option `2`, enter the expense ID, and provide the new description, amount, and category.

### Delete Expense

Select option `3`, enter the expense ID, and the selected expense will be removed.

### View Expenses

Select option `4` to display all recorded expenses in a table.

### Total Summary

Select option `5` to display:

- Total amount spent
- Total number of expenses

### Monthly Summary

Select option `6` and enter a month number from `1` to `12`. The program calculates the number and total value of expenses recorded in that month of the current year.

### Set Monthly Budget

Select option `7`, enter the month number and budget amount.

### Check Budget

Select option `8` to compare spending in the current month with the budget set for that month.

If spending is greater than the budget, the application displays a warning. Otherwise, it displays the remaining budget.

## Data Storage

This version stores expenses and budgets in Python lists and dictionaries while the program is running.

**Important:** Data is stored in memory only. When the program is closed, the recorded expenses and budgets are cleared. A database or file-based persistence system is not included in this version.

## Validation and Error Handling

The application handles common invalid inputs, including:

- Non-numeric expense amounts
- Non-numeric IDs
- Invalid month numbers
- Negative expense amounts
- Negative budgets
- Empty descriptions or categories
- Expense IDs that do not exist

## Technologies Used

- Python 3
- `datetime` module from the Python standard library
- Command-line interface (CLI)

## Project Execution

The project is designed to be fully executable through a terminal without requiring a graphical user interface.

## Submission Checklist

Before submitting the project:

- [ ] GitHub repository visibility is set to **Public**
- [ ] `README.md` is present at the repository root
- [ ] `main.py` is present at the repository root
- [ ] Project runs successfully using `python main.py`
- [ ] Repository root URL is submitted, not a `/tree/main/` or `/blob/` URL
- [ ] `PROJECT_REPORT.md` is included if the course submission requires a project report
- [ ] All files are committed and pushed to GitHub

## Author

Add your name, registration number, course, and institution here before submission.
