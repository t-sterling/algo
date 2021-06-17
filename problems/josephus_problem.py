"""
The josephus problem is:
    There are n people standing in a circle.
    Each person will kill the person to their right.
    This will continue until only 1 is left
    What position to stand in to be the survivor ?
"""


class Node(object):

    def __init__(self, val: int, nxt: 'Node' = None):
        self._val = val
        self._next = nxt

    @property
    def val(self) -> int:
        return self._val

    @property
    def next(self) -> 'Node':
        return self._next


def solve(n):

    head = None
    tail = None
    last = None
    for i in range(n):
        head = Node(n-i, tail)
        tail = head
        if last is None:
            last = tail

    last._next = head

    c = n
    while c > 0:
        head._next = head.next.next
        head = head.next
        c -= 1

    print(head.val)


if __name__ == "__main__":

    for i in range(3, 10):

        solve(i)
