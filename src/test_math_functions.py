import pytest
from math_functions import MathFunctions


def test_fibonacci():
    """
    This test check the fibonacci method

        assert math.calculate_fibonacci(0) == 0
    """
    math = MathFunctions()
    assert math.calculate_fibonacci(0) == 0
    assert math.calculate_fibonacci(1) == 1
    assert math.calculate_fibonacci(34) == 5702887


def test_factorial():
    """
    This test check the factorial method

        assert math.calculate_factorial(0) == 1
    """
    math = MathFunctions()
    assert math.calculate_factorial(0) == 1
    assert math.calculate_factorial(1) == 1
    assert math.calculate_factorial(5) == 120


def test_ackermann():
    """
    This test check the ackermann method

        math.calculate_ackermann(0, 0) == 1
    """
    math = MathFunctions()
    assert math.calculate_ackermann(0, 0) == 1
    assert math.calculate_ackermann(1, 0) == 2
    assert math.calculate_ackermann(3, 4) == 125

