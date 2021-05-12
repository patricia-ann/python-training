import os
os.system('cls')
# --- Example Program:
# ---Shape Area Calculator
#   The program should give a menu to the user to choose which shape to calculate,
#   then ask for the values (length, width, side etc.).
#   Using the values, return the calculated area.
#   Goal:
#    - Square  # Ask for the value of the side and return the calculated area
#    - Rectangle # Ask for the value of the length and width and return the calculated area
#    - Triange  # Ask for the value of the base and height and return the calculated area
#   Formulas:
#        Area of a Square = square of a side
#        Rectangle Area = length * width
#        Triangle Area = base * height / 2

print("Shape Area Calculator")
print("1)Square" + "\n" + "2)Rectangle" + "\n" + "3)Triangle")
shape = input("Enter the shape here: ")
if shape == '1':
    side = input("Enter the value for the side:   ")
    area = float(side)**2
elif shape == '2':
    length = input("Enter the value for the length:   ")
    width = input("Enter the value for the width:   ")
    area = float(length)*float(width)
elif shape == '3':
    base = input("Enter the value for the base:   ")
    height = input("Enter the value for the height:   ")
    area = (float(base)*float(height))/2
else:
    print("Invalid input!")
print(f"Area is {area}")
