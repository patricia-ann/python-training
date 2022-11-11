
import os 
os.system("clear")
# Files Handling
# Write, Read, and Delete

# Creating and Writing to file.
with open('mytest.txt', 'w') as file:
    file.write("This is the first line")

# # Appending to file.
# with open('mytest.txt', 'a') as file:
#     file.write("\nThis is the second line")
#     file.write("\nThis is the third line")

# # Reading a file.
# with open('mytest.txt', 'r') as file:
#     print(file.read())

# # Removing a file.
# os.remove('mytest.txt')
