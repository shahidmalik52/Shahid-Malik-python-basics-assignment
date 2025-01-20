# Part 6: Age Difference Calculator
# Write a program that:
# 1. Takes the ages of two people as input.
# 2. Calculates the difference in their ages using subtraction.
# Prints the result using string formatting:
# The age difference between [Person1] and [Person2] is: [Difference] years.

# Get inputs
age1 = int(input('Enter the age of Person1: '))
age2 = int(input('Enter the age of Person2: '))

# Calculate difference
difference = abs(age1 - age2)

# Print result
print(f'The age difference between [Person1] and [Person2] is {difference} years')