
def link(g, a, b):
    if a not in g.keys():
        g[a] = list()
    g[a].append(b)


class GraphBuilder(object):
    """
    links are one directional, ie. from src to tgt
    """

    def __init__(self):
        self._edges = list()

    def add_edge(self, src, tgt):
        self._edges.append([src, tgt])

    def add_edges(self, *args):
        for i in range(len(args)-1):
            self._edges.append([args[i], args[i+1]])

    def build_directed(self):
        
        g = dict()
        for e in self._edges:
            link(g, e[0], e[1])

        return g

    def build_undirected(self):

        g = dict()

        for e in self._edges:
            link(g, e[0], e[1])
            link(g, e[1], e[0])

        return g


def test_build():

    """
        a -> b
          -> c -> d -> f
    """

    builder = GraphBuilder()

    builder.add_edge("a", "b")
    builder.add_edge("a", "c")
    builder.add_edge("c", "d")
    builder.add_edge("d", "f")
    builder.add_edge("f", "a")

    print(builder.build_directed())

    print(builder.build_undirected())


if __name__ == "__main__":

    test_build()
