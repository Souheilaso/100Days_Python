def add(*args):
    result = 0
    for n in args:
        result += n
    # print(result)


add(1, 2)


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)