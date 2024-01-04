#!/usr/bin/python3

# print alphabet lowercase

print("{}".format("".join(chr(ord('a') + j) for j in range(26))), end="")
