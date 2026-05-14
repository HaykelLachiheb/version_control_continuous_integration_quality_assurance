import pytest
from calculator.utils import validate_number


class TestValidateNumber:
    def test_valid_integers(self):
        assert validate_number(5) is True
        assert validate_number(0) is True
        assert validate_number(-10) is True

    def test_valid_floats(self):
        assert validate_number(3.14) is True
        assert validate_number(-0.5) is True
        assert validate_number(0.0) is True

    def test_invalid_types(self):
        with pytest.raises(TypeError):
            validate_number("hello")
        with pytest.raises(TypeError):
            validate_number([1, 2, 3])
        with pytest.raises(TypeError):
            validate_number(None)
