

def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ", ".join(str(arg) for arg in args)
        kwargs_value =  ", ".join(f"{key}, {value}" for key, value in kwargs.items())

        print(f"{args_value} and {kwargs_value}")
        return func(*args, **kwargs)
    return wrapper



@debug
def greeting(name, greet = "Hello"):
    return f"{greet}, {name}"

print(greeting("Koushik"))