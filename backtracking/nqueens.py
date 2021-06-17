

"""
place n queens on an n*n board in positions such that not queens can attack another

x,0,0,0
0,0,x,0
0,0,0,0
0,X,0,0
"""


def solution(n):

    # key = y, val = x
    board = {}

    def is_safe(x, y):

        # position is occupied
        #
        if y in board and board[y] == x:
            return False

        # diagonals
        #
        if any([abs(by - y) == abs(board[by] - x) for by in board.keys()]):
            return False

        # horizontal and vertical
        #
        if any([by == y or board[by] == x for by in board.keys()]):
            return False

        return True

    def position(i):

        print(board)

        if i == n:
            return True

        for j in range(n):
            if is_safe(j, i):
                board[i] = j
                if position(i + 1):
                    return True
                else:
                    del board[i]

        return False

    return position(0)


if __name__ == "__main__":

    print(solution(20))