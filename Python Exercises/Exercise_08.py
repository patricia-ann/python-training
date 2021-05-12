import os
os.system('cls')
# Create a Python Program to convert a given temperature in celsius to fahrenheit
#    Note to convert temperatures in degrees Celsius to Fahrenheit, multiply by 1.8 (or 9/5) and add 32.
#    Example Input : 20
#    Example Output : 20 degrees Celsius is equivalent to 68.0 degrees in Fahrenheit


Cel = float(input("Enter the temperature in Celcius: "))
Far = Cel * 1.8 + 32
print(f"{Cel} degrees Celcius is equivalent to {Far} degrees in Farenheit")
