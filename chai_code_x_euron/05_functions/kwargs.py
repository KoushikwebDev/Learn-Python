

def newFunction(a, b, c):
    return a + b + c

print(newFunction(a=1, b=2, c=3))  # 6
# print(newFunction(c=3, a=1, b=2, d = 4))  # TypeError: newFunction() got an unexpected keyword argument 'd'


def kwargsFunction(**kwargs):
    for key, value in kwargs.items():
        print(f"Key : {key}, Value : {value}")
    return kwargs  # when we use **kwargs it is a dictionary of key-value pairs

print(kwargsFunction(a=1, b=2, c=3))  # {'a': 1, 'b': 2, 'c': 3}