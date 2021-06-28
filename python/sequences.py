"""
TODO: refresher on generator / iterator
"""


# generator functions
#
def squares_up_to(n):
    for i in range(n):
        yield i**2


# slicing
#
def slicing():

    items = [1, 5, 3]

    # reverse: the whole array, step back by -1 increment
    print(items[::-1])

    print(items[::-2])


def enumerate_example():
    """
    enumerate is handy for getting the index as we iterate through something

    :return:
    """

    sentence = "this is a sentence"

    for t in enumerate(sentence):
        print(f" {t[0]} + {t[1]}")

    print("-" * 10)

    # you can also offset the index
    #
    for t in enumerate("this is a sentence", -1):
        print(f" {t[1]} {sentence[t[0]]}")


def map_filter():
    """
    map and filter work in the expected way..
    :return:
    """

    # note, the use of the list constructor, not the literal. TODO: I don't know why.
    #
    print(list(filter(lambda i: i % 2 == 1, map(lambda a: ord(a), ['a', 'b', 'c']))))


if __name__ == "__main__":

    slicing()


