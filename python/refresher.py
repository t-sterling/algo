import datetime


def types():

    # str
    text = "almost before we knew it, we had left the ground"

    tokens = text.split(" ")
    print(tokens)
    tokens2 = list(tokens)
    tokens2.reverse()
    print(" ".join(tokens2))

    print(text[0: -len(tokens[len(tokens)-1])])
    print(text.replace("we", "they"))

    # numbers
    i = 2
    f = 1.5
    c = 1j

    # ops
    print(i * i)  # integer multiplication
    print(i * f)  # int float mult
    print(i * c)  # int complex mult
    print(f * c)  # float complex mult
    print(i / f)  # int float div
    print(i // f)  # int float integer division
    print(i ** i)  # int float power

    # datetime

    dt = datetime.datetime.strptime("2020:12:02", "%Y:%m:%d")

    print(dt.day)

    # how did that plus work ?
    plus_one_week = dt + datetime.timedelta(days=7)

    print(plus_one_week)


def functions():

    # inner functions
    def add_factory(n):

        # lambdas
        return lambda m: n + m

    add_five = add_factory(5)

    print(add_five(3))

    # named default params
    def say_hello(name: str = "no-one"):

        print(f"hello {name}")

    say_hello()

    say_hello(name="Jeff")

    # vargs
    def sum_of(*args):
        acc = 0
        for a in args:
            acc += a
        return acc

    print(sum_of(1, 2, 3, 4))

    # kwargs
    def person_to_string(name: str = None, age: int = None):

        return f"name: {name} age: {age}"

    print(person_to_string(name="Fred", age=12))

    def kwargs_example(**kwargs):

        print(kwargs)

    kwargs_example(name="bill", age=23)

    stan = {
        "name": "stan",
        "age": 43
    }

    print(type(stan))
    # expand an object into kwargs
    kwargs_example(**stan)

    # fails
    print(person_to_string(stan))
    # still fails
    print(person_to_string(*stan))
    # expands into named params
    print(person_to_string(**stan))


def builtins():

    print(abs(-1))

    print(all([True, False]))

    print(any([True, False]))

    print(bin(5))

    # boolean coercion
    print(bool("True"))
    print(bool("1"))
    print(bool("0"))
    print(bool("1231"))
    print(bool(""))

    class Runner(object):

        def __call__(self):

            print("hello from runner")

    r = Runner()
    r()
    print(callable(r))


def collections():

    # list

    # tuple

    # dict

    # set

    # deque

    # frozenset

    pass


def functools():

    # lambda

    # zip

    # map

    # reduce / fold

    pass


def main():

    # types()

    functions()

    # builtins()

if __name__ == "__main__":

    main()
