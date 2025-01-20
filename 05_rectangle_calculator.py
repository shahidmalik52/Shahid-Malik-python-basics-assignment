# Part 5: Rectangle Calculator
# Write a program that calculates and displays the area and perimeter of a rectangle:
# 1. Take the length and width of the rectangle as inputs.
# 2. Calculate the area and perimeter using basic arithmetic operators.
# Print the result in this format:
# - Length: [length]
# - Width: [width]
# - Area: [area]
# - Perimeter: [perimeter]
 
# Get inputs from user
length = float(input('Enter the length of rectangle: '))
width = float(input('Enter the width of rectangle: '))

# - Area: (A=l*w)
# - Perimeter: (P=2*(l+w))
area = length * width
perimeter = 2 * (length + width)

# Print the result in this format:
print(f"Length: {length} \nWidth: {width} \nArea: {area} \nPerimeter: {perimeter}")


