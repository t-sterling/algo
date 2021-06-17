from unittest import TestCase


def to_binary_string(num:int) -> str:
    """
    converts an int into it's binary representation
    """

    if num < 1:

        return ""

    else:

        return to_binary_string(int(num / 2)) + ("0" if num % 2 == 0 else "1");


class BinaryStringz(TestCase):

    def test_binary_string(self):

        self.assertEquals("1010", to_binary_string(4))

