
"""
solver for Tower of Hanoi problem
"""


class TowerOfHanoi(object):

    def __init__(self, size):

        self._size = size
        self._src = [i for i in range(size)]
        self._aux = list()
        self._dest = list()

    def solve(self):

        self._solve(self._size, self._src, self._aux, self._dest)

    def _solve(self, n, src, aux, dest):

        if n > 0:

            self._solve(n-1, src, aux, dest)

            self._dest.insert(0, src.pop())

            self._solve(n-1, aux, src, dest)

            print("-" * 5)
            print(src)
            print(aux)
            print(dest)
            print("-" * 5)


if __name__ == "__main__":

    tower = TowerOfHanoi(5)

    tower.solve()
