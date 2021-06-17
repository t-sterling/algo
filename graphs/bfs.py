"""
 BFS works by gathering all nodes at a layer before proceeding to the next layer
"""

import unittest
from graphs.graph import GraphBuilder
from typing import List


def bfs(graph, start, target):
    """
    bfs considers all nodes at a particular level before proceeding
    :param g:
    :param s:
    :param t:
    :return:
    """

    path: List = list()

    def _bfs(nodes: List[str]):
        """
        if any of the nodes are the target return path :: the node
        otherwise add the children to a new set of nodes to visit
        :param nodes:
        :return:
        """

        print(f"nodes: {nodes}")

        if len(nodes) == 0:
            return False

        to_visit = []

        for node in nodes:

            if node == target:

                path.append(node)
                return True

            else:

                if node in graph:
                    for child in graph[node]:
                        to_visit.append(child)

        return _bfs(to_visit)

    return _bfs(list(start))


class TestBFS(unittest.TestCase):

    def setUp(self):
        """
              a-cyclic directed graph
              a -> b -> c
                -> d
                -> e -> f -> g -> c
                          -> h -> d
        """

        builder = GraphBuilder()

        builder.add_edges("a", "b", "c")
        builder.add_edges("a", "d")
        builder.add_edges("a", "e", "f", "g", "c")
        builder.add_edges("f", "h", "d")

        self.graph = builder.build_directed()

        print(self.graph)

    def test_find(self):

        actual = bfs(self.graph, "a", "c")

        self.assertEqual(True, actual)

    def test_cant_find(self):

        actual = bfs(self.graph, "c", "d")

        self.assertEqual(False, actual)

    def test_cant_find_doesnt_exit(self):

        actual = bfs(self.graph, "a", "x")

        self.assertEqual(False, actual)
