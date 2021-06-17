

# TODO: remember that for gcd it takes 2 params, you switch them and the second is the i % j until the second is 0
#       Euclidean algorithm

def gcd(i: int, j: int) -> int:

    # i|j
    # -|-
    # 6|4
    # 4|2  <- 6 % 4 = 2
    # 2|0  <- 4 % 2 = 0
    #
    return i if j == 0 else gcd(j, i % j)


def gcd_iter(i: int, j: int) -> int:

    while j != 0:

        (i, j) = (j, i % j)

    return i


# TODO: it's easy, just multiply the 2 items and call gcd
#
def lcm(i: int, j: int) -> int:

    return int(i * j / gcd(i, j))


if __name__ == "__main__":

    print(gcd(6, 4))

    print(gcd_iter(6, 4))

    print(lcm(14, 16))


