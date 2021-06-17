
"""
    depth first search works on an a-cyclical directed graph

    visit each node of the graph recursively maintaining a path list
    if the target is found exit

"""

from graphs.graph import GraphBuilder
from typing import List


# TODO: non recursive version using a stack

def dfs(graph, start, target):

    _path: List = list()

    def _dfs(_node):

        print(f"node: '{_node}', path: {_path}")

        if _node == target:

            _path.append(_node)
            return

        elif _node in graph:

            children = graph[_node]

            _path.append(_node)

            for child in children:
                _dfs(child)
                if _path[-1] == target:
                    return

            _path.pop()

        return _path

    _dfs(_node=start)

    return _path


if __name__ == "__main__":

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

    g = builder.build_directed()

    print(g)

    path = dfs(graph=g, start="a",  target="g")

    print(path)

