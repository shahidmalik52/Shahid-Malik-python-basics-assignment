# Part 1: Temperature Comparison
# Write a program that:
# ● Takes input for the temperatures of two cities in Celsius.
# ● Compares the temperatures using relational operators (>, <, ==, !=).
# Prints a message like:
# City A is hotter than City B.

temp_A = int(input("Enter the temperature of City A in Celsius: "))
temp_B = int(input("Enter the temperature of City B in Celsius: "))

# compare tempratures one by one
# In Python, non-boolean values can also be used in and expressions, as Python will treat them according to their "truthiness":
# Non-zero numbers, non-empty strings, and non-empty containers (like lists, tuples, etc.) are considered True.
# Zero values (e.g., 0, None, [], '') are considered False.
# result = 5 and "Hello"
# print(result)  # Output: Hello

hotter = 'City A is hotter than City B'
cooler = 'City A is cooler than City B'
same = 'The termpartures of City A and City B are same'
result = (temp_A > temp_B and hotter) or (temp_A < temp_B and cooler) or (temp_A == temp_B and same)

# output the results
print(result)


