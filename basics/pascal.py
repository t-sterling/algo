
"""

Pascals triangle - related to the binomial coefficient

        1
      1   1
    1   2   1
  1   3   3   1
1   4   6   4   1

"""


def find_nth_row(n):
    """

    """
    if n == 1:
        return [1]

    elif n == 2:
        return [1, 1]

    last = find_nth_row(n - 1)

    return [1] + [last[i] + last[i+1] for i in range(0, len(last)-1)] + [1]


def find_nth_row_iter(n):

    rows = [[1], [1, 1]]
    if n == 1 or n == 2:
        return rows[n - 1]

    for i in range(2, n):
        last = rows[i - 1]
        rows.append([1] + [last[j] + last[j+1] for j in range(0, len(last)-1)] + [1])

    return rows[len(rows)-1]


if __name__ == "__main__":

    print(find_nth_row(8))

    print(find_nth_row_iter(8))
