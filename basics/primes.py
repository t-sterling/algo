
def sieve(n):
    """
    use sieve of Eratosthenes to return all primes under n
    :param n:
    :return:
    """
    
    # include 2 and start at 3 since 1 will modulo everything
    #
    primes = [2]
    for i in range(3, n):

        # test divisibility up to square root of i primes
        if not any([i % p == 0 for p in primes if p < i ** (1/2)]):
            primes.append(i)

    return primes


if __name__ == "__main__":

    print(sieve(1000))
