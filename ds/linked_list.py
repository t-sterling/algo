
import unittest
from typing import TypeVar, Generic

T = TypeVar('T')


class LinkedList(Generic[T]):
    """
    singly linked list implementation
    """

    def __init__(self, head, tail: 'LinkedList[T]' = None):
        self._head = head
        self._tail = tail

    def append(self, v: T) -> 'LinkedList[T]':
        t = self
        while t.tail is not None:
            t = t.tail
        n = LinkedList(v, tail=t._tail)
        t._tail = n
        return t

    def concat(self, other: 'LinkedList[T]') -> 'LinkedList[T]':
        n = self
        while n._tail is not None:
            n = n._tail
        n._tail = other
        return self

    @property
    def head(self) -> 'T':
        return self._head

    @property
    def tail(self) -> 'LinkedList[T]':
        return self._tail

    @tail.setter
    def tail(self, tail: 'LinkedList[T]'):
        self._tail = tail

    def __str__(self):
        return ",".join([self._head, str(self._tail if self._tail is not None else "")])


class TestLinkedList(unittest.TestCase):

    def test_add(self):

        llist: LinkedList[str] = LinkedList[str]("bill")

        self.assertEqual(llist.head, "bill")

        self.assertEqual(llist.tail, None)

        llist.append("frank")

        self.assertEqual(llist.tail.head, "frank")
