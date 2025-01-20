# Part 2: Bill Splitter
# Write a program that calculates how much each person needs to pay when splitting a bill:
# 1. Take the total bill amount as input.
# 2. Take the number of people as input.
# 3. Calculate each person’s share by dividing the total amount by the number of people.
# Print the result in this format:**
# Total Bill: $[amount]
# Number of People: [people]
# Each Person Pays: $[share]

# input total bill amount
total_bill = float(input("Enter the bill amount: "))

# input number of peoplele

no_of_people = int(input("Enter the number of people: "))

# calculate the share per person
bill_share = total_bill / no_of_people
bill_share

# Output the results in the given format
print(f"Total Bill: ${total_bill}")
print(f"Number of People: ${no_of_people}")
print(f"Each Person Pays: ${bill_share}")



