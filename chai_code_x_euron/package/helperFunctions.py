
from ..utils import methods # relative import from utils package

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b


def call_name_arr(name):
    return methods.name_arr(name)




# it is a good practice to include a main block in your script to prevent certain code from being run when the module is imported.
if __name__ == "__main__":
    print(add(2, 3))
    print(subtract(5, 3))