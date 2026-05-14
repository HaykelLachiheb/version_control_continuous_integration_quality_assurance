def validate_number(value):
    if not isinstance(value, (int, float)):
        raise TypeError(f"Expected a number, got {type(value).__name__}")
    return True
