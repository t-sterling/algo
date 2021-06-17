
"""
property of a binary tree is that nodes to the left represent values
less than those to the right

"""

from typing import TypeVar, Generic

K = TypeVar('K')
V = TypeVar('V')


class Node(Generic[K, V]):
    def __init__(self, k: K, v: V):
        self._key = k
        self._val = v


class BinaryTree(Generic[K, V]):

    def insert(self, k: K, v: V):
        pass

    def search(self, k: K):
        pass
