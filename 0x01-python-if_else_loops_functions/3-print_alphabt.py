#!/usr/bin/python3

# print alphabet leaving aout some characters

print("{}".format("".join(chr(ord('a') + j) for j in range(26)if chr(ord('a') + j) not in ['q', 'e'])), end="")
