# I. Python Syntax
# II. Variables and DataTypes
# a.Creating Variables

w = True  # Boolean
x = 12.12  # Float
y = "Hello"  # String

# Sequence Types
alphabets = ['a', 'b', 'c']  # List
fruits = ('a', 'b', 'c')  # Tuple
num = range(5)  # range

# Mapping Type
x = {"name": "John", "age": 36}  # Dictionary

# How to output the datatype
print(type(x))

# b.Assign to Mutiple Values
w, x, y = "100"  # assign same value to multiple variables
w, x, y = True, 12.12, "Hello"  # assign to multiple variables in one line.

# c.Casting and User Input
number1 = input("Enter your number: ")  # String
number2 = input("Enter your number: ")  # String
sum = int(number1) + int(number2)  # Convert to Integer
print(sum)
