def calculateMean(a, b):
    if a > b:
        print("a greater than b")
    else:
        print("b greater than a")
    x = (a + b) / 2
    return x


print(calculateMean(10, 3))
print(calculateMean(12, 23))


def abc(a):
    print(a)


# abc()


# ? Keyword argument


def sum(a, b):
    print(a + b)


sum(b=34, a=12)


def add(*numbers):
    print(type(numbers))
    print(numbers)  # (12, 23, 34, 45)
    sum = 0
    for x in numbers:
        sum += x

    print(sum)


add(12, 23, 34, 45)

# *numbers convert numbers into tuple


def convertIntoDic(**names):
    print(names)  # {'a': 'Koushik', 'b': 'Mou'}


convertIntoDic(a="Koushik", b="Mou")  # convertIntoDic(key="value", key="value")
