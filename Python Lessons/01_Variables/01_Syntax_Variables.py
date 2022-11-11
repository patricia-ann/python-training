from os import system
system("clear")

# I. Python Syntax - Comments, Indentation
# II. Variables and DataTypes
# a.Creating Variables

w = True  # Boolean
x = 12.12  # Float
y = "Hello"  # String
y = 'Hello'
b = '100'

# Type Casting
new_b = int(b)


# Sequence Types
alphabets = ['a', 'b', 'c']  # List
fruits = ('a', 'b', 'c')  # Tuple
num = range(5)  # range


# Mapping Type
person = {"name": "John", "age": 36}  # Dictionary

# print(x["name"], x["age"])

# How to output the datatype
# print(type(fruits))

# # b.Assign to Mutiple Values
a, b, c = True, 12.12, "Hello"  # assign to multiple variables in one line.

# # c.Casting and User Input
# number1 = input("Enter your 1st number: ")  # String
# number2 = input("Enter your 2nd number: ")  # String
# sum = int(number1) + int(number2)  # Convert to Integer
#print(sum)
