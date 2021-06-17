
"""
to use a list as a stack: append + pop. head is at end of list
to use a list as a queue: insert(0,n) + pop
TODO: tuples
"""

from collections import defaultdict

def default_dict_ex():

    counts = defaultdict()


def as_queue():

    chars = list('abcdef')

    q = list()

    for c in chars:
        q.insert(0, c)   # append at the end
        print(q)

    for i in range(5):
        print(q.pop())
        print(q)


def as_stack():

    stack = []

    chars = list('abcdef')

    for c in chars:
        stack.append(c)

    print(stack)

    while len(stack) > 0:
        print(stack.pop())


def concatenate_lists():

    a = [1, 2, 3]
    b = [4, 5, 6]

    print(a + b)


def default_dict():

    m = defaultdict(lambda: [])

    m[1].append(3)
    m[1].append(4)

    print(m)

    s = set()
    s.cl


def lists():

    name = "boris"

    l = []

    for i in range(len(name)):

        c = name[i]
        l.append(c)

    while l[0] != 'r':
        del l[0]
    del l[0]


    print(l)


if __name__ == "__main__":

    as_queue()
