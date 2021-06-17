

def rotate(m):
    """
    strategy is to cell by cell switch the items
    """
    if len(m) != len(m[0]):
        raise Exception("not a square matrix")

    for i in range(len(m)):

        pass
        # TODO: finish this.. I can't get my head around the transform


if __name__ == "__main__":

    m = [['a','b'], ['c', 'd']]
    # m = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
    print(rotate(m))

