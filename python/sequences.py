"""
TODO: refresher on generator / iterator
"""


# generator functions

def squares_up_to(n):
    for i in range(n):
        yield i**2


if __name__ == "__main__":

    for s in squares_up_to(20):
        print(s)
