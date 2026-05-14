# QA Report

## Project: Calculator Application

### 1. Unit Tests Written

| Test File | Test Name | Description | Status |
|-----------|-----------|-------------|--------|
| tests/test_basic.py | test_add | Verifies addition of integers, floats, negatives, and zeros | ✅ |
| tests/test_basic.py | test_subtract | Verifies subtraction of integers, floats, and zeros | ✅ |
| tests/test_basic.py | test_multiply | Verifies multiplication of integers, floats, negatives, and zeros | ✅ |
| tests/test_basic.py | test_divide | Verifies division of integers and floats | ✅ |
| tests/test_basic.py | test_divide_by_zero | Verifies ValueError raised on division by zero | ✅ |
| tests/test_basic.py | test_average | Verifies average of integers, single element, floats, and negatives | ✅ |
| tests/test_basic.py | test_average_empty | Verifies ValueError raised for empty list | ✅ |
| tests/test_advanced.py | test_power | Verifies exponentiation, zero exponent, and fractional exponent | ✅ |
| tests/test_advanced.py | test_sqrt | Verifies square root of positive numbers and zero | ✅ |
| tests/test_advanced.py | test_sqrt_negative | Verifies ValueError raised for sqrt of negative | ✅ |
| tests/test_advanced.py | test_modulo | Verifies modulo operation on integers and floats | ✅ |
| tests/test_advanced.py | test_modulo_by_zero | Verifies ValueError raised for modulo by zero | ✅ |
| tests/test_advanced.py | test_factorial | Verifies factorial of 0, 1, 3, and 5 | ✅ |
| tests/test_advanced.py | test_factorial_invalid | Verifies ValueError raised for negative factorial | ✅ |
| tests/test_advanced.py | test_factorial_non_integer | Verifies ValueError raised for non-integer factorial | ✅ |
| tests/test_utils.py | test_valid_integers | Verifies validate_number passes for integer inputs | ✅ |
| tests/test_utils.py | test_valid_floats | Verifies validate_number passes for float inputs | ✅ |
| tests/test_utils.py | test_invalid_types | Verifies TypeError raised for string, list, and None | ✅ |

**Total Tests: 18 (all passing)**

### 2. Linter Results (flake8)

| Check | Status | Issues Found |
|-------|--------|--------------|
| Code style consistency | ✅ | No style violations detected |
| Line length violations | ✅ | No lines exceeding 100 characters |
| Unused imports | ✅ | No unused imports found |
| Syntax errors | ✅ | No syntax errors detected |

**Summary:** The codebase passes all flake8 checks with zero warnings. The code follows PEP 8 conventions consistently across all modules. The `--max-line-length=100` setting was respected throughout.

### 3. Code Review Summary

| PR # | Reviewer | Key Feedback | Changes Made |
|------|----------|--------------|--------------|
| #1 | Peer Reviewer | "The `average()` function correctly handles edge cases like empty lists, but consider using `statistics.mean` for production use" | Kept custom implementation for educational purposes, added docstring |
| #2 | Peer Reviewer | "Good test coverage for edge cases (empty list, single element, floats)" | No changes needed - tests were comprehensive |

**Key Improvements from Code Reviews:**
- Added error handling for empty list input in `average()` based on discussion
- Improved test coverage from 16 to 18 tests after peer review session
- Standardized error messages to use consistent pattern: "Cannot compute ..."

---

*Report prepared by: Haykel Lachiheb*
