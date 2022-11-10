from os import system

system("clear")
# Strings
# a.Assign String to Variable
greet = 'Hello'

# b.Multiline Strings

greetings = """ 
Hello
Konnichiwa
Bonjour
"""

# c.String Length
print(len(greet))

# d.Slicing
print(greet[1:4])
print(greet[:4])
print(greet[1:])
print(greet[-2:])

# e.Check String
if 'Hello' in greetings:
    print("Hello is a greeting")

# f.Modify Strings
g_u = greet.upper()
g_l = greet.lower()
g_r = greet.replace('e', 'a')

# g.Concatenation
print("Hello" + " World!")

# h.Format Strings
quantity = 3
item = 4
sum_num = 3 + 4

print("Quantity is {}, item is {} and the sum is {}".format(quantity, item, sum_num))
print(f"Quantity is {quantity}, item is {item} and the sum is {sum_num}")

# i.Escape Characters
txt = "We are the so-called \n \"Vikings\" from the north."
print(txt)

# j.String Methods ()
# Refer to [https://docs.python.org/3/library/string.html]
