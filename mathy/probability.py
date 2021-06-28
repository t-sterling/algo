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
    def _fact(_n):
        acc = 1
        while _n > 0:
            acc *= _n
            _n -= 1
        return acc

    return _fact(n) / _fact(k) * _fact(n - k)


def NChooseK(n, k):
    """

    generate all combinations of k in n in lexicographical order

    [1,2,3] choose 2:
    1,2
    1,3
    2,3

    to lexicographically order, start with left, iterate the remainder



    """

    pass


def combinations(items, k):
    """
    delegate to the generator and use it to index into items
    """

    pass


def permutations(items):
    """
    generate all permutations in lexicographical order
    :param items:
    :return:
    """
    pass

"""
class TestProbability(unittest.TestCase):

    def test_binomial_coefficient(self):

        print(binomial_coefficient(3, 2))
"""


def pairs(items):
    """
    find all pairs in items
    :param items:
    :return:
    """

    # how to generalize ?
    """
        5 choose 3
        need an array of indexes
        items = [1,2,3,4,5]
        idx =   [1,2,3]
        
        [1,2,3]
        [1,2,4]
        [1,2,5]
        [1,3,4]
        [1,3,5]
        [1,4,5]
        [2,3,4]
        [2,3,5]
        [2,4,5]
        [3,4,5]
        
        
        
    """
    for i in range(len(items)):
        for j in range(i+1, len(items)):
            yield items[i], items[j]


if __name__ == "__main__":

    """
    for pair in pairs(['a', 'b', 'c', 'd', 'e', 'f', 'g']):
        print(pair)
    """
    print(binomial_coefficient(5, 3))




