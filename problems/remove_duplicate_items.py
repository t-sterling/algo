"""
remove duplicates from a linked lsit
"""
import unittest


class Node(object):

    def __init__(self, val, tail: ['Node'] = None):

        self._val = val
        self._tail = tail

    @property
    def val(self):
        return self._val

    @property
    def tail(self) -> 'Node':
        return self._tail

    @tail.setter
    def tail(self, tail: ['Node']):
        self._tail = tail

    def __str__(self):
        return f"[val: {self.val}] -> {self.tail}"


def _(val, tail: ['Node'] = None):
    return Node(val, tail)


def remove_duplicates(head):
    vals = set()
    n = head
    p = None
    while n is not None:
        if n.val in vals:
            p.tail = n.tail
        else:
            vals.add(n.val)
        p = n
        n = n.tail


def remove_duplicates_no_buffer(head):

    """
    todo: 2 pointers runs in n^2, for each node iterate the whole thing
    :param head:
    :return:
    """
    pass


class TestSolution(unittest.TestCase):

    def test_remove_duplicates(self):

        llist = _("a", _("b", _("b", _("c"))))

        expected = "[val: a] -> [val: b] -> [val: c] -> None"

        remove_duplicates(llist)

        actual = str(llist)

        self.assertEqual(actual, expected)

    def test_remove_duplicates_no_buffer(self):

        llist = _("a", _("b", _("b", _("c"))))

        expected = "[val: a] -> [val: b] -> [val: c] -> None"

        remove_duplicates_no_buffer(llist)

        actual = str(llist)

        self.assertEqual(actual, expected)

