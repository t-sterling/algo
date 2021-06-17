
# how to round to the nearest n



def rounder(n, m):

    print((m - (m % n)))
    i = (m - (m % n)) / 3

    print(i)


if __name__ == "__main__":

    # 3 10
    rounder(3, 10)
