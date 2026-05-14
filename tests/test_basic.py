import pytest
from calculator.basic import add, subtract, multiply, divide, average


class TestBasicOperations:
    def test_add(self):
        assert add(2, 3) == 5
        assert add(-1, 1) == 0
        assert add(0, 0) == 0
        assert add(1.5, 2.5) == 4.0

    def test_subtract(self):
        assert subtract(5, 3) == 2
        assert subtract(0, 5) == -5
        assert subtract(10, 10) == 0
        assert subtract(2.5, 1.5) == 1.0

    def test_multiply(self):
        assert multiply(3, 4) == 12
        assert multiply(0, 5) == 0
        assert multiply(-2, 3) == -6
        assert multiply(2.5, 2) == 5.0

    def test_divide(self):
        assert divide(10, 2) == 5
        assert divide(7, 2) == 3.5
        assert divide(0, 5) == 0
        assert divide(-6, 3) == -2

    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)

    def test_average(self):
        assert average([1, 2, 3, 4, 5]) == 3
        assert average([10]) == 10
        assert average([1.5, 2.5]) == 2.0
        assert average([-1, 0, 1]) == 0

    def test_average_empty(self):
        with pytest.raises(ValueError, match="Cannot compute average of an empty list"):
            average([])
