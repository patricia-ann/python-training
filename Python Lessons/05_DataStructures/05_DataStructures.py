import os
os.system('cls')
# Data Structures

## a. LISTS
fruits_list = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
numbers = [1, 2, 3, 4]

# Access List
print(fruits_list[1])
print(fruits_list[:3])

# Add new item to list
fruits_list.append('watermelon')
fruits_list.insert(6, 'wintermelon')

# Updating the list
fruits_list[6] = "pineapple"

# Remove an item on a list
fruits_list.pop(2)

# Loop thru List
for t in fruits_list:
    print(t)

# Join two lists
print(fruits_list + numbers)

# Sort Lists
fruits_list.sort()  # Default is Ascending
fruits_list.sort(reverse=True)  # Descending Sort
fruits_list.reverse()  # Reverse the original order of string last to first


## b. TUPLES
numbers = (10, 11, 12, 13)

# Accessing and Looping same with List
# Changing items in a Tuple is not allowed

# Unpack Tuples
(a, b, c, d) = numbers
print(a)
print(b)


## c. DICTIONARY
car_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# Access Dictionary
print(car_dict["brand"])

# Add items in a dictionary
car_dict['description'] = "car"

# Change items in a dictionary
car_dict.update({"year": 2020})

# Remove items in a dictionary
car_dict.pop("model")

# Loop thru a Dictionary
print("Printing the keys in a dictionary: ")
for k in car_dict.keys():
    print(k)

print("Printing the values in a dictionary: ")
for v in car_dict.values():
    print(v)

print("Printing the keys and values in a dictionary: ")
for k, v in car_dict.items():
    print(k, v)
