#!/usr/bin/python3

"""
    program that imports functions from the file calculator_1.py,
    does some Maths, and prints the result.
"""

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    add_reslt = add(a, b)
    sub_reslt = sub(a, b)
    mul_reslt = mul(a, b)
    div_reslt = div(a, b)

    print("{:d} + {:d} = {:d}".format(a, b, add_reslt))
    print("{:d} - {:d} = {:d}".format(a, b, sub_reslt))
    print("{:d} * {:d} = {:d}".format(a, b, mul_reslt))
    print("{:d} / {:d} = {:d}".format(a, b, div_reslt))
