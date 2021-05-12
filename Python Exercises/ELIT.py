import os
os.system('cls')

i = 0
level = 20

while i < level:   # 5 times at leaast
    spaces = level - i
    stars = " "*spaces + "* "*i
    i += 1
    print(stars)
