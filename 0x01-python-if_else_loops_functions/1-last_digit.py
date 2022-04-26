#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
less_than_six = "and is less than 6 and not 0"
if number % 10 == 0:
    print(f"Last digit of {number} is {number % 10} and is 0")
elif number < 0:
    print(f"Last digit of {number} is -{-number % 10} {less_than_six}")
else:
    if number % 10 < 6:
        print(f"Last digit of {number} is {number % 10} {less_than_six}")
    else:
        print(f"Last digit of {number} is {number % 10} and is greater than 5")
