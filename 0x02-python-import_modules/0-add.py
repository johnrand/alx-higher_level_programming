#!/usr/bin/python3

"""Program to import modules

    Add():
        calling a function
"""
a = 1
b = 2
add_0 = __import__('add_o')
result = add_0.add(a, b)
print("{} + {} = {}".format(a, b, result))
