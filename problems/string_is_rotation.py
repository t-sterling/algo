import unittest


class Solution(object):

    @staticmethod
    def is_rotation(s1, s2) -> bool:

        return s1 in (s2 * 2)


class TestSolution(unittest.TestCase):

    def test_is_rotation(self):

        actual = Solution().is_rotation("hello", "ohell")

        self.assertTrue(actual)

    def test_is_not_rotation(self):

        actual = Solution().is_rotation("hello", "help")

        self.assertFalse(actual)
