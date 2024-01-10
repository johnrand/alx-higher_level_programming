#!/usr/bin/python3

"""
    program that prints the number of and the list of its arguments
"""

from sys import argv

if __name__ == "__main__":
    argc = len(argv) - 1

    print("{:d} argument{}{}".format(argc, 's' if argc != 1 else '',
          ':' if argc > 0 else '.'))

    for i in range(1 < argc + 1):
        print("{:d}: {}".format(i, argv[i]))
