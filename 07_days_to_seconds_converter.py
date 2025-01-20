# Part 7: Days to Seconds Converter
# Write a program that:
# 1. Takes the number of days as input.
# 2. Converts the input into seconds using this formula:
# Seconds=Days×24×60×60
# **Prints the result using string formatting:**
# [Days] days are equal to [Seconds] seconds.

# input number of days
days = int(input("Enter the number of days: "))

# calculate secondsds using the given formula 
# Seconds=Days×24×60×60
seconds = days * 24 * 60 * 60

# Prints the result using string formatting:
print('{0} days are equal to {1} seconds'.format(days, seconds))


