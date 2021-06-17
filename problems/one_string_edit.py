"""
detect if a string is 1 'string-edit' from another
"""

import math
import unittest
from collections import defaultdict


def is_insert_edit(longer, shorter) -> bool:
    """
    are all but 1 the same ?
    :param longer:
    :param shorter:
    :return:
    """
    count = defaultdict(bool)

    for i in range(len(longer)):
        count[longer[i]] = True

    for i in range(len(shorter)):
        count[shorter[i]] = False

    return sum(count.values()) == 1


def is_insert_edit_2(longer, shorter) -> bool:
    """
    alternative implementation takes n
    :param longer:
    :param shorter:
    :return:
    """
    idx_longer = 0
    idx_shorter = 0
    while idx_shorter < len(shorter) and idx_longer < len(longer):
        if longer[idx_longer] != shorter[idx_shorter]:
            if idx_shorter != idx_longer:
                return False
            idx_longer += 1
        else:
            idx_longer += 1
            idx_shorter += 1
    return True


def is_replace_edit(s1, s2) -> bool:
    """
    is one character different?
    :param s1:
    :param s2:
    :return:
    """
    diff = False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if diff:
                return False
            diff = True
    return diff


def is_one_edit(s1, s2) -> bool:

    # if they're the same no edits..
    #
    if s1 == s2:
        return False

    # if they're more than 1 size diff, it's more than 1 edit
    #
    if math.fabs(len(s1) - len(s2)) > 1:
        return False

    # if they're the same size, check if it's 1 replacement
    #
    if len(s1) == len(s2):
        return is_replace_edit(s1, s2)

    # if 1 is 1 char longer than the other check if that char can just be inserted
    #
    elif len(s1) == len(s2) + 1:
        return is_insert_edit_2(s1, s2)
    elif len(s2) == len(s1) + 1:
        return is_insert_edit_2(s2, s1)
    return False


class TestStringEditDetector(unittest.TestCase):

    def test_large_diff(self):
        actual = is_one_edit("a", "bcde")
        self.assertFalse(actual)

    def test_replace(self):
        actual = is_one_edit("tim", "tom")
        self.assertTrue(actual)

    def test_delete(self):
        actual = is_one_edit("tim", "tm")
        self.assertTrue(actual)

    def test_insert(self):
        actual = is_one_edit("tim", "time")
        self.assertTrue(actual)

    def test_insert(self):
        actual = is_one_edit("etim", "tim")
        self.assertTrue(actual)

    def test_2_edits(self):
        actual = is_one_edit("tim", "lime")
        self.assertFalse(actual)
