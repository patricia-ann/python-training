import os
os.system('cls')
# Print the number 250000 as currency with the thousands grouped by commas.
# Currency should be displayed with two decimal places and begin with the US dollar symbol.
# Expected Output: $250,000.00
mynum = 250000
print(f"${mynum:,.2f}")
