
import unittest
from collections import defaultdict


class Solution(object):

    @staticmethod
    def are_palindromes(words):
        """
        so.. count the non whitespace letters. if there are an even number for every character and possible 1 odd
        then palindromes can be formed
        :param words:
        :return:
        """
        flags = defaultdict(bool)
        for c in list(words):
            if c != ' ':
                flags[c] = not flags[c]

        return 0 <= sum(flags.values()) <= 1


class TestPalindromePermutations(unittest.TestCase):

    def test_are_palindromes(self):

        actual = Solution().are_palindromes("tact coa")
        self.assertTrue(actual)

    def test_are_not_palindromes(self):

        actual = Solution().are_palindromes("pigeon food")
        self.assertFalse(actual)
