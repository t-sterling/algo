

# TODO: lookup interval trees

def arrayManipulation(n, queries):

    arr = [0] * n
    for i in queries:
        print(i)
        for j in range(n+1):
             if j >= i[0] and j <= i[1]:
                arr[j-1] += i[2]
        print(arr)
    return max(arr)


if __name__ == "__main__":

    print(arrayManipulation(4, [[2, 3, 603], [1, 1, 286], [4, 4, 882]]))
