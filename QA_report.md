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

**Total Tests: 16**

### 2. Linter Results (flake8)

| Check | Status | Issues Found |
|-------|--------|--------------|
| Code style consistency | ✅ / ❌ | _(Describe any style issues found)_ |
| Line length violations | ✅ / ❌ | _(List files and lines)_ |
| Unused imports | ✅ / ❌ | _(List unused imports)_ |

**Summary:** _(Overall assessment of code style quality)_

### 3. Code Review Summary

| PR # | Reviewer | Key Feedback | Changes Made |
|------|----------|--------------|--------------|
| #1 | _(Name)_ | _(Feedback)_ | _(Changes)_ |
| #2 | _(Name)_ | _(Feedback)_ | _(Changes)_ |

**Key Improvements from Code Reviews:**
- _(List improvements made after peer reviews)_

---

*Report prepared by: [Your Name]*
