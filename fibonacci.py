def fibonacci(n):
    r"""Calculates Fibonacci numbers"""
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
