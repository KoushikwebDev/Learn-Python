# def inner():
#     print(2 + 3)


# def higherFunction(fn):
#     fn()


# higherFunction(inner)


def higher():
    def inner():
        print("inner...function")

    return inner


x = higher()
x()


def uppercase_decorator(func):
    print("upper")

    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result

    return wrapper


@uppercase_decorator
def greet():
    return "hello, world!"


print(greet())


list1 = [1, 2, 3, 4, 5, 6]


def calculateSum(list1):
    sum = 0
    for ele in list1:
        sum += ele
    return sum


totalSum = calculateSum(list1)
print(totalSum)
