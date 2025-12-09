import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#in memory storage
expenses = []

#system for adding expenses 
def add_expenses():
    item = input("Item: ")
    amount = input("Amount: ")
    category = input("Category: ")
    date = input("Date (YYYY-MM-DD): ")

    expenses.append({
        "item": item,
        "amount": amount,
        "category": category,
        "date": date
    })
    print("Expenses added!")

#system for viewing expenses
def view_expenses():
    if not expenses:
        print("No expenses found")
        return
    df = pd.DataFrame(expenses)
    print("Your expenses")
    print(df)
    print()

#system for deleting expenses
def delete_expenses():
    if not expenses:
        print("No expenses to delete")
        return
    df = pd.DataFrame(expenses)
    print("Your expenses:")
    print(df)

    index = input("Enter the index of the expense to delete: ")

    if not index.isdigit():
        print("Invalid input. Please enter a number.")
        return

    index = int(index)

    if index not in df.index:
        print("Invalid index. No expense deleted.")
        return

    df = df.drop(index).reset_index(drop=True)

    global expenses
    expenses = df.to_dict(orient="records")
    print("Expense deleted!") 