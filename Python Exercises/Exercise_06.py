# Given a string as input, output a string made of 3 copies of the last 2 chars of the original string.
# Example Input : 'Hello'
# Expected Output: 'lololo'

my_string = input("Enter any string here:")
print(my_string[-2:]*3)
