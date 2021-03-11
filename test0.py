from prime import *


def test_prime(n, expected):
    if is_prime(n) != expected:
        print(f"Error on is prime({n}), expected {expected}")
