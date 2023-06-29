def add(n1, n2):
    return n1 + n2


def diff(n1, n2):
    return n1 - n2


def multiplication(n1, n2):
    return n1 * n2


def division(n1, n2):
    return n1 // n2


with open('test.txt') as f:
    for line in f:
        data = line.split()
        a = int(data[0])
        b = int(data[1])

addV = add(a, b)
diffV = diff(a, b)
multiplicationV = multiplication(a, b)
divisionV = division(a, b)
