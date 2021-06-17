
# memoize results for the recursive version
#
fib_rec_mem = {}


def fib_recursive(n):

    if n in fib_rec_mem:
        return fib_rec_mem[n]
    if n == 0 or n == 1:
        return n
    else:
        fib_rec_mem[n-1] = fib_recursive(n - 1)
        fib_rec_mem[n-2] = fib_recursive(n - 2)
        return fib_rec_mem[n-1] + fib_rec_mem[n-2]


def fib_iterative(n):

    acc = 2
    fibs = [1, 1]
    while acc < n:
        fibs.append(fibs[acc - 1] + fibs[acc - 2])
        acc += 1

    return fibs[acc - 1]


if __name__ == "__main__":

    print(fib_iterative(7))
