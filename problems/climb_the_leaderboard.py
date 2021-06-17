"""

An arcade game player wants to climb to the top of the leaderboard and track their ranking. The game uses Dense Ranking, so its leaderboard works like this:

The player with the highest score is ranked math  on the leaderboard.
Players who have equal scores receive the same ranking math, and the next player(s) receive the immediately following ranking math.
Example



The ranked players will have ranks , , , and , respectively. If the player's scores are ,  and , their rankings after each game are ,  and . Return .

"""

"""
current_rank = 1
prev_rank = -1

for ranked_score in ranked:

    if player_score >= ranked_score:
        return current_rank

    if prev_rank == -1 or prev_rank > current_rank:
        current_rank += 1
    prev_rank = current_rank

return current_rank

THIS DOESN'T WORK

"""

import bisect


def climbingLeaderboard(ranked, player):

    # strategy:
    #   condense the ranks so we know rank by index
    #   for each score binary search the ranks

    _ranked = list(set(ranked))
    _ranked.reverse()
    print(_ranked)

    def get_rank(score):

        index = len(_ranked) - bisect.bisect_right(ranked, score)

        print(index)

        if index >= len(_ranked):
            return index + 1

        if score == _ranked[index]:
            return index

        elif score < _ranked[index]:
            return index + 2


    ret = []

    for p in player:
        ret.append(get_rank(p))

    return ret


if __name__ == "__main__":

    res = climbingLeaderboard([100, 90, 90, 80], [70, 80,105])

    print(res)

    print(res == [4, 3, 1])
