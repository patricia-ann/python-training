from os import system
system("clear")
#####################################################################################
# Write a function named 'calculation' such that it can accept two variables and calculate the addition and subtraction of them.
# And also it must return both addition and subtraction in a single return call
# Example: 
    # Enter first number: 100
    # Enter 2nd number : 3
# Expected Output: 103, 97


# Your Code here
def calculation(num1, num2):
    result1 = num1 + num2
    result2 = num1 - num2
    print(f"Expected output is: {result1}, {result2}")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter 2nd number: "))

calculation(num1, num2)


