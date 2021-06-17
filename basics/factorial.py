
"""

factorials recursively and iteratively

factorial is a number times all the numbers smaller
needed in calculating combinations/permutations

4! = 4 * 3 * 2 * 1 = 24

"""


def fact_recursive(n):
    if n < 2:
        return 1
    return n * fact_recursive(n-1)


def fact_iterative(n):
    acc = 1
    while n > 0:
        acc *= n
        n -= 1
    return acc


if __name__ == "__main__":

    print(fact_iterative(4))