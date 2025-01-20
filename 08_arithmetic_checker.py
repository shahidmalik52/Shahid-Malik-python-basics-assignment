# Part 8: Arithmetic Checker
# Write a program that:
# 1. Takes two numbers as input.
# 2. Prompts the user to input an arithmetic operator (+, -, *, /).
# Performs the operation on the numbers and prints the result.
# [Number1] [Operator] [Number2] = [Result]

# Get inputs
num1 = int(input('Enter the first num: '))
num2 = int(input('Enter the second num: '))
operator = input('Enter the opertor: ')

# Perform the operation
# In Python, non-boolean values can also be used in and expressions, as Python will treat them according to their "truthiness":
# Non-zero numbers, non-empty strings, and non-empty containers (like lists, tuples, etc.) are considered True.
# Zero values (e.g., 0, None, [], '') are considered False.
# result = 5 and 2
# print(result)  # Output: Hello


result = (operator == '+' and num1+num2) or (operator == '-' and num1-num2) or (operator == '*' and num1*num2) or (operator == '/' and num1/num2)

# output the results
print('{0} {1} {2} = {3}'.format(num1, operator, num2, result))