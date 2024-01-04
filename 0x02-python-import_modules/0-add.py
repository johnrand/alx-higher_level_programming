#!/usr/bin/python3

"""Program to import modules
    
    Add():
        calling a function
"""

a = 1
b = 2

add_0 = __import('add_o').add
print(f"{a} + {b} = {add(a, b)}")
