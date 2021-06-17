
"""
given an array determine if it contains 2 elems that add up to a num

e.g:

[1,2,3] and 4 = 1+3

[1,2,3] and 6 is false

"""


def two_sum(_ints, _target):

    # hashing solution
    #
    vals = set()
    for i in _ints:
        if _target - i in vals:
            return [_target - i, i]
        vals.add(i)

    return None


if __name__ == "__main__":

    print(two_sum([1, 2, 3], 1))
    print(two_sum([1, 2, 3], 2))
    print(two_sum([1, 2, 3], 3))
    print(two_sum([1, 2, 3], 4))
    print(two_sum([1, 2, 3], 5))
    print(two_sum([1, 2, 3], 6))
