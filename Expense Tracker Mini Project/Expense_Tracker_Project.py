# Author: Shahid Malik
# Project Title:
# "Expense Tracker and Financial Health Checker"

# Objective:
# The goal of this project is to build a simple Expense Tracker that allows a user to input their
# income, expenses, and savings goals. The program will then provide real-time insights into
# their financial health by analyzing their data using strings, operators, and conditional
# statements (including nested if-else).

# 1. User profile setup
    # ● Ask the user to input their name and profession.
    # ● Display a personalized welcome message.

name = input("Please enter your name: ")
profession = input("Please enter your profession: ")
print(f"Welcome, {name}! Let's analyze your financial health as a {profession}")

# 2. Income and Expense Management:
#     ● Ask the user for their monthly income and monthly expenses.
#     ● Calculate the savings (Income - Expenses).
#     ● Use arithmetic operators to calculate the percentage of income saved.

monthly_income = int(input('Mmonthly income: '))
monthly_expense = int(input('Monthly expenses: '))
savings = monthly_income - monthly_expense
savings_percentage = int((savings / monthly_income )* 100)
print(f'Total Savings: {savings} \nSavings Percentage: {savings_percentage}%')

# Financial Health Check:
#     ● Use nested if-else conditions to provide insights based on the savings percentage:
#     ○ If savings are greater than or equal to 20% of income:
#           ■ Print: "Great job, [Name]! You have a strong savings habit."

#     ○ If savings are between 10% and 20%:
#           ■ Print: "Good, [Name], but you could save a bit more."

#     ○ If savings are less than 10%:
#           ■ Print: "Warning, [Name]: Your savings are too low. Consider cutting expenses!"

if savings_percentage >= 20:
    print(f'Great Job, {name}! You have a strong savings habit.')
elif 10 <= savings_percentage < 20:
    print(f'Good, {name}, but you could save a bit more.')
elif savings_percentage < 10:
    print(f'Warning, {name}: Your savings are too low. Consider cutting expenses!')

# Categorize Expenses:
# ● Ask the user to categorize their expenses into three major areas:
#   1. Essentials (e.g., rent, utilities, groceries)
#   2. Wants (e.g., dining out, entertainment)
#   3. Savings/Investments

while True:
    essential_expense = int(input('How much do you spend on Essential? '))
    wants_expense = int(input('How much do you spend on Wants? '))
    # savings_investment = int(input('How much do you Save or invest? '))

    essential_expense_percentage = (essential_expense/monthly_income)*100
    wants_expense_percentage = (wants_expense/monthly_income)*100
    # saving_investment_percentage = (savings_investment/monthly_income)*100

    if monthly_expense == (essential_expense + wants_expense):
        print(f'Expense Breakdown: \nEssentials: {essential_expense_percentage}% \nWants: {wants_expense_percentage}% \nSavings/Investments: {savings_percentage}%')
        break
    else: 
        print('Your entered breakdown of expenses is invalid')

# Custom Goals:
#   ● Allow the user to input a savings goal (in percentage).
#   ● Use conditional logic to evaluate if they are meeting their goal:
#   ○ If the current savings percentage is greater than or equal to the goal:
#       ■ Print: "Congratulations, [Name]! You’ve achieved your savings goal."
#   ○ Else:
#       ■ Print: "Keep working on your savings, [Name]. You're [X]% away from your goal

saving_goal = int(input("What is your Savings goal (in %)? "))
if savings_percentage >= saving_goal:
    status = f"Congratulations, {name}! You've achieved your savings goal." 
    print(status)
else:
    status = f"{saving_goal - savings_percentage}% away from your goal"
    print(f"Your savings percentage is {savings_percentage}% \nKeep working on your savings, {name}. You're " + status)

# Export Summary (Bonus Feature):
# ● Generate a summary of the user’s financial health in a formatted string or save it to a text file.

# Financial Health Summary for Sarah:
# Income: 80000
# Expenses: 60000
# Savings: 20000 (25%)
# Expense Breakdown:
# Essentials: 50%
# Wants: 18.75%
# Savings/Investments: 31.25%
# Savings Goal: 30%
# Status: 5% away from your goal.

print(f'Financial Health Summary for {name}:')
print(f'Income: {monthly_income} \nExpenses: {monthly_expense} \nSavings: {savings} ({savings_percentage}%) ')
print(f'Expense Breakdown: \nEssentials: {essential_expense_percentage}% \nWants: {wants_expense_percentage}%')
print(f'Savings/Investments: {savings_percentage}% \nSavings Goal: {saving_goal}% \nStatus: {status}')
