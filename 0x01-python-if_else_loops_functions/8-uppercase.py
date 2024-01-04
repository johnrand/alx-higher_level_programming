#!/usr/bin/python3

# print a string in uppercase

def uppercase(s):

    result = ""

    for c in s:

        result += "{:c}".format(ord(c) - 32) if 97 <= ord(c) <= 122 else c

    print(result + "\n", end="")
