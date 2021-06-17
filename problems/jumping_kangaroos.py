

def kangaroo(x1, v1, x2, v2):

    if v1 > v2:
        while x1 < x2:
            x1 += v1
            x2 += v2
    return "YES" if x1 == x2 else "NO"


if __name__ == "__main__":

    print(kangaroo(21, 6, 47, 3))

# TODO: understand this math
# (x1-x2) % (v2-v1) == 0 and v1>v2
