# Part 4: Two-Number Relationship
# Write a program that:
# 1. Takes two numbers as input.
# 2. Checks and displays their relationship using these conditions:
# Whether the first number is greater than, less than, or equal to the second number.
# Whether both numbers are even or odd.
# Print the results in this format:
# Number 1: [num1]
# Number 2: [num2]
# Relationship: [Greater than/Less than/Equal]
# Both numbers are [Even/Odd/Mixed].

# get inputs
num1 = int(input('Enter 1st num: '))
num2 = int(input('Enter 2nd num: '))

# check relationship w.r.t greater, less, equal
result1 = (num1 > num2 and 'Greater than') or (num1 < num2 and 'Less than') or (num1 == num2 and 'Equal')

# check relationship w.r.t even, odd
result2 = ((num1 % 2 == 0 and num2 % 2 == 0) and 'Even') or ((num1 % 2 != 0 and num2 % 2 != 0) and 'Odd') or ((num1 % 2 == 0 and num2 % 2 != 0) and 'Mixed') or ((num1 % 2 != 0 and num2 % 2 == 0) and 'Mixed') 

# print results
print('Number 1: {0} \nNumber 2: {1} \nRelationship: {2} \nBoth numbers are {3}'.format(num1, num2, result1, result2))