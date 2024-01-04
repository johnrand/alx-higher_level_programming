#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

last_digit = abs(number) % 10
sign = '-' if number < 0 else ''

if last_digit == 0:
    sign = ''

output_string = (
        f"Last digit of {number} is {sign}{last_digit}"
        )
if last_digit > 5:
    output_string += " and is greater than 5"
elif last_digit == 0:
    output_string += " and is 0"
else:
    output_string += " and is less than 6 and not 0"

print(output_string)
