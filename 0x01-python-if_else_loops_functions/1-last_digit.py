#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
sign = '-' if number < 0 else ''
#more if statement
if abs(number) % 10 > 5:
    print(f"Last digit of {number} is {sign}{abs(number) % 10} and is greater than 5")
if abs(number) % 10 == 0:
    print(f"Last digit of {number} is {sign}{abs(number) % 10} and is 0")
if abs(number) % 10 < 6 and abs(number) % 10 != 0:
    print(f"Last digit of {number} is {sign}{abs(number) % 10} and is less than 6 and not 0")

