#!/usr/bin/python3

"""Program to import modules

    Add():
        calling a function
"""
if __name__ == "__main__":
    from add_0 import add

    a = 1
    b = 2
    result = add(a, b)
print("{} + {} = {}".format(a, b, result))
