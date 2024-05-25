class Calculator:
    def _validate_numbers(*args):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError(f"All arguments must be numbers, but got {type(arg).__name__}")

    def add(a, b):
        Calculator._validate_numbers(a, b)
        return a + b

    def subtract(a, b):
        Calculator._validate_numbers(a, b)
        return a - b

    def multiply(a, b):
        Calculator._validate_numbers(a, b)
        return a * b

    def divide(a, b):
        Calculator._validate_numbers(a, b)
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
