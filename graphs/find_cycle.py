
import unittest
from graphs.graph import GraphBuilder


def find_cycle(graph, start):
    """
    bfs, stops when a cycle is detected or there are no more children
    """
    visited = set()

    def _find_cycle(nodes):

        print(nodes)

        if len(nodes) == 0:
            return False

        to_visit = set()
        for node in nodes:
            if node in visited:
                return True
            else:
                visited.add(node)
                if node in graph:
                    children = graph[node]
                    for child in children:
                        to_visit.add(child)

        return _find_cycle(to_visit)

    return _find_cycle(set(start))


class TestFindCycle(unittest.TestCase):

    def setUp(self):
        """
        a -> b -> c -> d -> b
        """
        builder = GraphBuilder()
        builder.add_edges("a", "b", "c", "d", "b")
        self.graph = builder.build_directed()
        print(self.graph)

    def test_detects_cycle(self):

        actual = find_cycle(self.graph, "a")
        self.assertEqual(True, actual)
