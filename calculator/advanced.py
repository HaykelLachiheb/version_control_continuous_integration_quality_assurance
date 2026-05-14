def power(base, exp):
    return base ** exp


def sqrt(value):
    if value < 0:
        raise ValueError("Cannot compute square root of a negative number")
    return value ** 0.5


def modulo(a, b):
    if b == 0:
        raise ValueError("Cannot compute modulo by zero")
    return a % b


def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Factorial is defined only for non-negative integers")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
