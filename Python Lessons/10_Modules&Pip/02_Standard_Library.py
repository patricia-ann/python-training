# https://docs.python.org/3/tutorial/modules.html#standard-modules
# We can use Standard Libraries or Build-In Python modules using import.

# In here we are importing the built-in os, glob, datetime and math modules
# More built in modules can be found here -> https://docs.python.org/3/library/
import os
import glob
import math
from datetime import date


# using system function of os module to use a command to clear the terminal
os.system('cls')

# using glob to find files with .txt extension
print(glob.glob('*.txt'))

# using sqrt function of math module to pass a command and clear the terminal
print(math.sqrt(64))

# Using date function of datetime module to output the date today.
print(date.today())
