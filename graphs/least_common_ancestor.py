"""
given 2 nodes in an a-cyclical graph, find the common parent
"""

from graphs.graph import GraphBuilder

# TODO: for this to work, node needs to know it's parent for direction

def least_common_ancestor(g, n1, n2):


    pass


if __name__ == "__main__":

    """
        a -> b -> c -> d
               -> e
    """

    builder = GraphBuilder()
    builder.add_edges("a", "b", "c", "d")
    builder.add_edges("b", "e")

    print(least_common_ancestor(builder.build_undirected(), "e", "d"))

