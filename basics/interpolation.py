

def linear_interp(v, x1, x2, y1, y2):

    return y1 + ((y2 - y1) / (x2 - x1)) * v


if __name__ == "__main__":

    print(linear_interp(50, 0, 100, 50, 100))
