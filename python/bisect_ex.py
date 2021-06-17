

import bisect


def test_bisect():

    example = [1, 3, 4]

    #print(bisect.bisect_right(example, 2))
    #print(bisect.bisect_left(example, 2))

    print(bisect.bisect(example, 2))

if __name__ == "__main__":

    test_bisect()


