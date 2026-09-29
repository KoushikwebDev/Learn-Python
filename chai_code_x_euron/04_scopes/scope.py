def num():
    name = 3.14159265

# print(name)  # error: name 'name' is not defined


x = 99

def func():
    global x  # this tells Python that we want to use the global variable x
    x = 100  # this will change the global variable x
    print(x)  # 100

func()
print(x)

def func2():
    x = 10
    # global x  # "x" is assigned before global declaration
    print(x)


# closure example or factory function example
def func3():
    x = 10
    def func4():
        return x  # this will return the value of x from the enclosing scope (func3)
    return func4

print(func3()())  # 10


def func5(num):
    def func6(x):
        return x ** num
    return func6

func5(3)(2)  # 8