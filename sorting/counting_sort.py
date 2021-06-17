
from typing import List
import random


"""

    TODO: I don't really see the point
    
"""


def counting_sort(unsorted: List[int], k: int):

    # ma
    output = [0] * k

    for i in unsorted:
        output[i] += 1

    for i in range(1, len(unsorted)):
        output[i] += output[i-1]

    return output


if __name__ == "__main__":

    test_input = random.sample(range(0, 10), 10)

    print(test_input)
    k = len(set(test_input))
    output = counting_sort(test_input, k)
    print(output)
