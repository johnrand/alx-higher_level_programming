#!/usr/bin/python3

# function to remove a character at a given position

def remove_char_at(str, n):
    if 0 <= n < len(str):
        return str[:n] + str[n+1]
    else:
        return str
