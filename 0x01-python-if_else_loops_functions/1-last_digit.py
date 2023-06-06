#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lD = number % 10
if lD > 5:
    print(f"Last digit of {number} is {lD} and is greater than 5")
if lD == 0:
    print(f"Last digit of {number} is {lD} and is 0")
if lD < 6 and lD != 0:
    print(f"Last digit of {number} is {lD} and is less than 6 and not 0")
