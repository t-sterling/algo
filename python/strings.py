
from collections import defaultdict

def sort_a_string(string):

    print(sorted(string))


def escape_sequences():

    pass


def reverse_string():

    pass


def comparison():

    pass


def formatting():

    pass


def find_in():

    pass


def is_palindrome(string):

    size = len(string)
    for i in range(size // 2):
        if string[i] != string[(size-1) -i]:
            return False
    return True


def char_array(note):

    needed = defaultdict(int)
    for c in list(note):
        needed[c] += 1

    print(needed)


if __name__ == "__main__":

    #char_array("this is some text")

    sort_a_string("helllo")

"""
if __name__ == "__main__":

    print(is_palindrome(""))
    print(is_palindrome("ab"))
    print(is_palindrome("aba"))
    print(is_palindrome("abba"))
    print(is_palindrome("abcba"))
    print(is_palindrome("abcdba"))
    print(is_palindrome("abac"))
"""