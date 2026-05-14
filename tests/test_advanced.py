import pytest
from calculator.advanced import power, sqrt, modulo, factorial


class TestAdvancedOperations:
    def test_power(self):
        assert power(2, 3) == 8
        assert power(5, 0) == 1
        assert power(10, 1) == 10
        assert power(4, 0.5) == 2.0

    def test_sqrt(self):
        assert sqrt(9) == 3
        assert sqrt(0) == 0
        assert sqrt(2) == pytest.approx(1.414, 0.001)
        assert sqrt(0.25) == 0.5

    def test_sqrt_negative(self):
        with pytest.raises(ValueError, match="Cannot compute square root of a negative number"):
            sqrt(-1)

    def test_modulo(self):
        assert modulo(10, 3) == 1
        assert modulo(10, 5) == 0
        assert modulo(7, 2) == 1
        assert modulo(2.5, 1) == 0.5

    def test_modulo_by_zero(self):
        with pytest.raises(ValueError, match="Cannot compute modulo by zero"):
            modulo(5, 0)

    def test_factorial(self):
        assert factorial(0) == 1
        assert factorial(1) == 1
        assert factorial(5) == 120
        assert factorial(3) == 6

    def test_factorial_invalid(self):
        with pytest.raises(ValueError, match="Factorial is defined only for non-negative integers"):
            factorial(-1)

    def test_factorial_non_integer(self):
        with pytest.raises(ValueError, match="Factorial is defined only for non-negative integers"):
            factorial(3.5)
