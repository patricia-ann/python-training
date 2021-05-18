# Write a function named 'calculation' such that it can accept two variables and calculate the addition and subtraction of them.
# And also it must return both addition and subtraction in a single return call
# Expected Output: 50, 30


# Your Code here
def calculation(num1, num2):
    sum = num1 + num2
    diff = num1 - num2
    return sum, diff


res = calculation(40, 10)
print(res)
