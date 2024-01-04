#!/usr/bin/python3

# print a string in uppercase

def uppercase(s):
    for c in s:
        print("{:c}".format(ord(c) - 32)if 97 <= ord(c) <= 122 else c, end="\n")
