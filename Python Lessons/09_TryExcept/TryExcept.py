from os import system
system("clear")

# Try, Except and Finally
# https://docs.python.org/3/tutorial/errors.html#handling-exceptions
# Example code which loops until you enter a valid number
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError as error:
        print("Please enter a valid number! ", error)
    finally:  # Statements under finally will always run regardless if there's an error catched or not.
        print("The End.")
