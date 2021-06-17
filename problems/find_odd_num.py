

def find_odd(items):
    """
    test to see if the smallest bit is 1
    """
    r = [i for i in items if i & 1 == 1]

    print(r)


if __name__ == "__main__":

    items = [2, 4, 8, 5, 10, 12]

    find_odd(items)
