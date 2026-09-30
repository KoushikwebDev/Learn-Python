def check_input(value):
    if not isinstance(value, int):
        raise ValueError("Input must be an integer.")
    return value

print(check_input(10))  # Valid input
# print(check_input("invalid"))  # Raises ValueError


# custom exception example
class CustomError(Exception):
    def __init__(self, message, length):
        super().__init__(f"CustomError: {message} requires length {length}.")

def validate_length(password):
    if len(password) < 8:
        raise CustomError("Password", 8)

# print(validate_length("short"))  # Raises CustomError


try:
    validate_length("short")
except CustomError as e:
    print(e)  # Output: CustomError: Password requires length 8.

# Assertion example

def divide(a, b):
    assert b != 0, "Division by zero is not allowed."
    return a / b

print(divide(10, 0))  # Raises AssertionError
# print(divide(10, 2))  # Output: 5.0