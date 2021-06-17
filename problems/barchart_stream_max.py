
"""
CMC Markets interview question - hard

You receive an infinite stream of integers. Maintain the max rectangle observed so far, for example:

    3223123

    #  #  #
    #### ##
    #######

For that example, the max rect so far is 8.

"""


class Solution(object):

    def __init__(self):

        self._observations = {}
        self._max = -1

    def accept(self, n: int):
        """
        Each n represent the next height of a bar in a barchart.
        Maintain the max rectangular are observed in the bar chart so far.
        :param n:
        :return:
        """

        # add to the observations if not present
        #
        if n not in self._observations:
            self._observations[n] = 0

        # copy everything the same or lower
        #
        clone = {k: v for (k, v) in self._observations.items() if k <= n}

        # increment all
        #
        for k in range(n, 0, -1):
            clone[k] = (clone[k] if k in self._observations else 0) + 1

        # calculate the max
        #
        new_max = max([k * clone[k] for k in clone])

        if new_max > self._max:
            self._max = new_max

        self._observations = clone

        print(self._observations)

    @property
    def max(self):
        return self._max


if __name__ == "__main__":

    s = Solution()
    for n in [3, 2, 2, 3, 1, 2, 3]:

        s.accept(n)

    print(s.max)
