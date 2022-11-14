from os import system

system("clear")
# https://docs.python.org/3/tutorial/modules.html
# Modules can be used to create reusable functions on a separate file which can be imported to our main python file or to other python files we may have.
# In this way, we keep our code maintainable and easy to read.

# Assuming Modules.py is our main python file, we can then use the functions from fibonnaci.py
# Note that fibonnaci.py should be on same directory as the main file.

# Using fibonnaci module on the main python file, and adding alias called fib
import fibonnaci as fib

# Another way to use the fibonnaci module by specifying the functions to use
from fibonnaci import fib1, fib2
# if we import it as above, we can directly call the function name. ex. result = fib1(10)

# Use dot notation to access the functions and pass the result to the variables.
# https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/ 
# Identifier to let interpreter know the parts to be excuted when invoked directly, and when imported

if __name__ == "__main__":
    result = fib.fib1(10)
    result2 = fib.fib2(10)
    print(result)
    print(result2)

