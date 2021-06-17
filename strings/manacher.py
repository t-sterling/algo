
"""
The idea of Manachers algorithm is:

    you start with the n ** 2 solution, checking if each center is a palindrome, left to right:

    0 1 2 3 4 5 6 7 8 9 10
    |           |
    a b a x a b a x a b b
    | | | |
    1 3 1 7 .. what next ?

    if you find a palindrome, how do you pick the next spot to check from, the next center?
    If you can find a sub palindrome in the left side when mirrored to the right side takes you at least to the right
    edge, then take that as the new center.

    0 1 2 3 4 5 6 7 8 9 10
    |           |
    a b a x a b a x a b b
    | * |   | * |

    So then check around that center:
    0 1 2 3 4 5 6 7 8 9 10
    |           |
    a b a x a b a x a b b
      |       *       |

...

   ok, but what about:

   a b c d e f e d c b a

   the only palindrome is around the f so it's worst case and intuitively I'd think this would be the most common case.

"""


def manacher(s):

    assert set.isdisjoint({'$', '^', '#'}, s)
    if len(s) == 0:
        return 0, 1
    t = "^#" + "#".join(s) + "#$"
    c = 1
    d = 1
    p = [0] * len(t)
    for i in range(2, len(t) - 1):
        mirror = 2 * c - i
        p[i] = max(0, min(d - i, p[mirror]))
        while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
            p[i] += 1
        if i + p[i] > d:
            c = i
            d = i + p[i]
    k, i = max((p[i], i) for i in range(1, len(t) - 1))

    return (i-k) // 2, (i + k) // 2


def test(test):
    print(test)
    sub = manacher(test)
    print(test[sub[0]:sub[1]])


if __name__ == "__main__":

    test("abcdefedc")
    test("abcdefghijklmn")
    #test("babcbabcbaccba")