import unittest

"""

permuatations:
    - order doesn't matter
    - with repetition:      n ^ k
    - without repetition:   n! / (n-k)!


combinations
    - order does matter
"""


def binomial_coefficient(n, k):
    """

    binomial coefficient is how many combinations of k are in n:
       n! / k! * (n-k)!

    :param n:
    :param k:
    :return:
    """
    def fact(_n):
        acc = 1
        while _n > 0:
            acc *= _n
            _n -= 1
        return acc

    return fact(n) / fact(k) * fact(n - k)


def NChooseK(n, k):
    """
    generate all combinations of k in n in lexicographical order

    :param n:
    :param k:
    :return:
    """
    pass


def combinations(items, k):
    """
    delegate to the generator and use it to index into items
    :param items:
    :param k:
    :return:
    """

    pass


def permutations(items):
    """
    generate all permutations in lexicographical order
    :param items:
    :return:
    """
    pass


class TestProbability(unittest.TestCase):

    def test_binomial_coefficient(self):

        print(binomial_coefficient(3, 2))


