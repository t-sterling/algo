

from ds.linked_list import LinkedList
import unittest


def remove_nth_element(ll: LinkedList, n: int):

    if ll.tail is None:
        raise Exception("cannot delete from a list with only 1 elem")

    i = 0
    t: LinkedList = ll
    p: LinkedList = None
    while i < n:
        i += 1
        p = t
        t = t.tail
        if t is None:
            raise Exception(f"index out of range: {n}")

    p.tail = t.tail


class TestRemoveNthElem(unittest.TestCase):

    def test_delete_last_elem(self):

        ll = LinkedList[str]("bob").append("shiella")

        remove_nth_element(ll, 1)

        self.assertEqual("bob,", str(ll))

    def test_delete_middle(self):

        ll = LinkedList[str]("bob").append("shiella").append("frank")

        remove_nth_element(ll, 1)

        self.assertEqual("bob,frank,", str(ll))
