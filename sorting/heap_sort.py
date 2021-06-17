
import unittest


class Heap(object):

    def __init__(self, capacity: int):

        self._arr = [None] * capacity

    def parent(self, i:int):
        if i // 2 >= 0:
            return self._arr[i // 2]
        return None

    def left(self, i: int):
        if 2 * i < len(self._arr):
            return self._arr[2 * i]
        return None

    def right(self, i: int):
        if 2 * i + 1 < len(self._arr):
            return self._arr[2 * i + 1]



class HeadTest(unittest.TestCase):

    def test_heap_add(self):

        pass
