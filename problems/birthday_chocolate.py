


def birthday(s, d, m):

    def sums_to(items, target):
        sum = 0
        for i in items:
            sum += i
            if sum > target:
                return False
        return sum == target

    ret = []

    for i in range(len(s) - (m-1)):
        ss = s[i: i+m]
        if sums_to(ss, d):
            ret.append(ss)

    return ret


if __name__ == "__main__":

    s = [2, 2, 1, 3, 2]

    print(s)

    print(birthday(s, 4, 2))
