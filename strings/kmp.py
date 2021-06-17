
# Knuth Morris Pratt

def maximum_border_path(w):
    """
    a boundary is a substring that is found in both prefix and suffix position
    this computes the maximum boundaries
    """

    n = len(w)
    f = [0] * n
    k = 0
    for i in range(1, n):
        while w[k] != w[i] and k > 0:
            k = f[k - 1]
        if w[k] == w[i]:
            k += 1
        f[i] = k
    return f


if __name__ == "__main__":
    t = "abaababaa"
    print(maximum_border_path(t))

