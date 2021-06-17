import sys


# Complete the blacklist function below.
#
def blacklist(amounts):

    def cheapest(n, k):

        c = float('inf')

        for j in range(k):
            if amounts[1 + j][n] < c :
                c = amounts[1 + j][n]

        return c

    n = amounts[0][0]
    k = amounts[0][1]

    acc = 0
    for i in range(n):
        acc += cheapest(i, k)

    print(acc)


if __name__ == "__main__":

    amounts = [
        [3, 2],
        [1, 4, 2],
        [2, 2, 2]
    ]

    blacklist(amounts)
