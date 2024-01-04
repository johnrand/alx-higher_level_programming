#!/usr/bin/python3

# print alphabet in reverse and alternate lower with upper

for i in range(ord('z'), ord('A') - 1, -1)[:26]:
    print("{}".format("".join(chr(i) if i % 2 == 0 else chr(i - 32))), end="")
