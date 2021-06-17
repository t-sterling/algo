from collections import deque

"""
To and from binary strings iteratively and recursively
"""


def from_binary_str(candidate: str):

    if len(candidate) == 0:

        return 0

    # take the first elem, (i.e. zero or one) and multiply it by 2 to the power of the math of remaining digits
    #
    # 101            01             1
    # 1 * (2 ** 2) + 0 * (2 ** 1) + 1 * (2 ** 0)
    # 1 * 4        + 0 * 2        + 1 * 1        = 4 + 1 = 5
    #
    return int(candidate[0]) * int(2 ** (len(candidate) - 1)) + from_binary_str(candidate[1:len(candidate)])


def from_binary_str_iter(candidate: str):

    chars = deque([int(s) for s in candidate])
    acc = 0
    while len(chars) > 0:
        c = chars.popleft()
        acc += c * int(2 ** len(chars))

    return acc


def to_binary_string(n: int):

    if n < 1:

        return "0"

    # head recursive:
    #
    # to_binary_string(5) -> "1"
    # to_binary_string(2) -> "0
    # to_binary_string(1) -> "1"
    # to_binary_string(0) -> "0"
    #
    # 0101 = 5
    #
    return to_binary_string(int(n/2)) + str(0 if n % 2 == 0 else 1)


def to_binary_str_iter(n: int):

    if n == 0:
        return "0"

    chars = ""
    while True:
        chars = str(0 if n % 2 == 0 else 1) + chars
        if n < 1:
            break
        n //= 2

    return chars


if __name__ == "__main__":

    for i in range(100):

        js = to_binary_string(i)

        print(str(i) + " " + str(js))

        j = from_binary_str(js)

        ks = to_binary_str_iter(j)

        k = from_binary_str_iter(ks)

        print(k)


"""
01011110
     100
"""