#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
a = str(number)[-1]
if int(a) > 5:
    print(f"{str(a)} is greater than 5")
elif int(a) == 0:
    print(f"{str(a)} is 0")
elif 0 < int(a) < 6:
    print(f"{str(a)} is less than 6 and not 0")


