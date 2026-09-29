# positional only arguments
def positional_only(a, b, /):
    return a + b


# keyword only arguments
def keyword_only(*, a, b):
    return a + b


# positional and keyword arguments
def positional_and_keyword(a, *, b):
    return a + b

# default arguments
def default_args(a, b=10):
    return a + b


# variable length arguments
def variable_length_args(*args):
    return args


# variable length keyword arguments
def variable_length_kwargs(**kwargs):
    return kwargs

def example(positional, *args, keyword_only=None, **kwargs):
    pass


# function call
print(positional_only(1, 2))  # 3
print(keyword_only(a=1, b=2))  # 3
print(positional_and_keyword(1, b=2))  # 3
print(default_args(1))  # 11
print(variable_length_args(1, 2, 3))  # (1, 2, 3)
print(variable_length_kwargs(a=1, b=2))  # {'a': 1, 'b': 2}