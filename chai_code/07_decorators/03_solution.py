import time

def cache(func):
    cache_value = {}
    def wrapper(*args):
        args_value = ", ".join(str(arg) for arg in args)

        if args_value in cache_value:
            return cache_value[args_value]
        
        result = func(*args)
        cache_value[args_value] = result

        return result

    return wrapper


@cache
def long_running_function(a, b):
    time.sleep(4)
    return a + b

print(long_running_function(2,3))
print(long_running_function(2,3))
print(long_running_function(2,3))
print(long_running_function(2,3))
print(long_running_function(2,3))
print(long_running_function(2,3))
print(long_running_function(2,3))
