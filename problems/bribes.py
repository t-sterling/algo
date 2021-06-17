

def minimumBribes(q):

    min_bribes = 0

    for i in range(len(q)):

        # check that no value is > than it's index+2
        if q[i] > i + 3:
            print("Too chaotic")
            return

        """
        # the number of bribes is the sum of differences between value and index ?
        if q[i] > (i+1):
            min_bribes += q[i] - (i+1)
        """

        # todo: for each q[i] need to count everything between positions q[i]-1 and i, if it is > the add it
        #       it means: since p[i] == i at the start then the max 2 bribes can make is p[i] = p[i-1] therefore
        #       count everthing that is > in that range

    print(min_bribes)


if __name__ == "__main__":

    minimumBribes([1, 2, 5, 3, 7, 8, 6, 4])

"""
0: 1 2 3 4 5 6 7 8
          -
1: 1 2 3 5 4 6 7 8
        -
2: 1 2 5 3 4 6 7 8
              -
3: 1 2 5 3 4 7 6 8
            -
4: 1 2 5 3 7 4 6 8
                -
5: 1 2 5 3 7 4 8 6
              -
6: 1 2 5 3 7 8 4 6
                -
7: 1 2 5 3 7 8 6 4
"""