import os
os.system('cls')
# Control Flows - https://docs.python.org/3/tutorial/controlflow.html
# If..Else
num = 100

if num == 100:
    print("number is equal to 100!")
elif num < 100:  # elif is short for else if
    print("number is less than 100!")
elif num > 10:  # even if this is true for the above num, this is not printed since the if condition is already true
    print("number is greater than 10")
else:
    print("The End!")


# While
# Used for repeated execution as long as an expression is true
print("Using while loop to execute until 4!")
num = 0
while num < 5:
    print(num)
    num += 1  # add 1 to num each loop

print("Using break to halt the loop and continue to skip an iteration")
num2 = 0
while num2 < 10:
    num2 += 1
    if num2 == 1:
        continue
    elif num2 == 5:
        break
    print(num2)


# For Loops
# Looping through string
print("Looping through a string!")
my_string = "PYTHON"
for i in my_string:
    print(i)
# For the examples to loop thru list, tuple and dictionary, refer to DataStructures Lesson

# range() can be used to generate arithmetic progressions
print("Using range to print hello 3 times")
for i in range(3):
    print("hello", i)

print("Using break and continue in a for loop")
for my_num in range(10):
    if my_num == 1:
        continue
    elif my_num == 5:
        break
    print(my_num)


# Using List Comprehension to create a new list
numbers = [1, 2, 3, 4]
# created a new list called squares from numbers list
squares = [i**2 for i in numbers]

# Enumerate
cities = ['Manila', 'Pasig', 'Mandaluyong']
print("Using enumerate to loop thru a list and output the index and list values!")
for index, c in enumerate(cities):
    print(index, c)


# Zip
names = ['Peter Parker', 'Clark Kent', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Batman']

print("Using zip to loop thru multiple list!")
for name, hero in zip(names, heroes):
    print(f"{name} is actually {hero}")
