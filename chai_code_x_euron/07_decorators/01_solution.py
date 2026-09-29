import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} Execution time: {end - start}")
        return result
    return wrapper


@timer # it is equivalent to example_function = timer(example_function)
def example_function(n):
    time.sleep(n)
    return n

print(example_function(2))  # example_function Execution time: 2.002345323562622


# definination of decorators
# here besically when we are calling a function then we can run another function with some extra logic as per our need, its like a higher order function
