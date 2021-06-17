from basics.binary import *

# TODO: https://www.geeksforgeeks.org/category/algorithm/bit-magic/


def pprint(s):

    print(s.rjust(10))


def nums():

    # arithmetic shift
    #
    n = 100
    pprint(str(n))
    pprint(to_binary_string(n))
    print(10 * "-")

    # half
    pprint(to_binary_string(n >> 1))
    pprint(str(n >> 1))
    print(10 * "-")

    # double
    pprint(to_binary_string(n << 1))
    pprint(str(n << 1))
    print(10 * "-")


def set_nth_bit(x, n):

    return x | (1 << n)


def unset_nth_bit(x, n):

    return x & (1 << n)


def toggle_nth_bit(x, n):

    return x ^ (1 << n)


def int_equality(i, j):

    return (i ^ j) == 0


def check_int_is_odd(n):

    return n & 1


def both_have_same_sign(i, j):

    return (i ^ j) >= 0


def flip_the_sign(n):

    return ~n + 1


def is_power_2(n):

    return n > 0 & (n & (n - 1)) == 0


def increment(n):

    return -~n


def decrement(n):

    return ~-n


if __name__ == "__main__":

    pprint(str(to_binary_string(1 & 0)))
    pprint(str(to_binary_string(1 & 1)))

    pprint(str(to_binary_string(1 | 0)))
    pprint(str(to_binary_string(1 | 1)))

    pprint(str(to_binary_string(~0)))
    pprint(str(to_binary_string(~1)))

    pprint(str(to_binary_string(1 ^ 0)))
    pprint(str(to_binary_string(1 ^ 1)))
