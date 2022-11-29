from os import system
system("clear")

# Functions - https://docs.python.org/3/tutorial/controlflow.html#defining-functions


# Declaring a sum function which accepts a and b arguments
def sum(a, b):
    result = a + b
    return result  # returning the result variable


# Calling the sum function and output the result
#print(sum(10, 12))


# Default Argument Values
# In here, we assign category with default value as Non-Fiction
def book_info(book_name, category='Non-Fiction'):
    book_category = category
    output = f"The book name is {book_name}, category is {book_category}"
    return output


# Since category value was not passed, category is assigned to the default value.
#print(book_info('Power of Habit'))


# Arbitrary Arguments *args can be used to pass varying nunber of positional arguments
def my_sum(*args):
    result = 0
    # Iterating over the Python args tuple
    for x in args:
        result += x # result = result + x 
    return result

#print("Sum is", my_sum(1, 2, 3, 10, 11, 12))


# Keyword Arguments **kwargs works just like args but instead of accepting positional arguments, it accepts keyword arguments

def my_book(**kwargs):
    return f"Book name is {kwargs['name']}, category is {kwargs['category']}, author is {kwargs['author']}"

print(my_book(name="The Outliers", category="Non-Fiction", author="Malcolm Gladwell"))
