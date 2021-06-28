
import unittest
from ds.linked_list import LinkedList


def len_of_ll(ll: LinkedList):

    i = 1
    t: LinkedList = ll
    while t.tail is not None:
        i += 1
        t = t.tail

    return i


class TestLinkedList(unittest.TestCase):

    def setUp(self):

        self._ll = LinkedList[str]("bob").append("dave").append("jane")

    def test_len(self):

        actual = len_of_ll(self._ll)

        self.assertEqual(3, actual)

