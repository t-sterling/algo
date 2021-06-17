
"""
can't remember the actual problem for this one..
"""


def predict(offset):

    p = 1
    acc = 0
    inc = 0

    while offset > 0:

        base = 10 ** p
        d = 1.0 / p
        if offset - base > 0.0:
            inc = base * d
            offset -= base
        else:
            inc = offset * d
            offset -= inc / d

    acc += inc
    p += 1

    return int(acc)
    

def main():

    results = [(x, predict(x)) for x in range(150)]

    print(results)


if __name__ == "__main__":

    main()
