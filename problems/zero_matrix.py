import unittest


class Solution(object):

    @staticmethod
    def zero(m):
        """
        job of this method is to set all in the col and row to zero when it encounters a zero
        :param m:
        :return:
        """
        zeros = {}
        for r in range(len(m)):
            for c in range(len(m[0])):
                if m[r][c] == 0:
                    zeros[r] = c

        for rr, cc in zeros.items():
            for r in range(len(m)):
                m[r][cc] = 0
            for c in range(len(m[rr])):
                m[rr][c] = 0

        return m


class TestSolution(unittest.TestCase):

    def test_zero(self):

        test = [
            [1, 2, 3],
            [3, 0, 5],
            [6, 7, 8]
        ]

        expected = [
            [1, 0, 3],
            [0, 0, 0],
            [6, 0, 8]
        ]

        actual = Solution().zero(test)

        self.assertEqual(expected, actual)
