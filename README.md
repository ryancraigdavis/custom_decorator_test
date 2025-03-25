# Decorator Test Repository

This repository demonstrates the implementation and testing of a custom decorator in Python, showcasing best practices for decorator design and testing.

## Structure

- `decorator.py` - Contains the implementation of the custom decorator
- `decorator_usage.py` - Demonstrates usage of the decorator
- `test_decorator.py` - Unit tests for the decorator itself
- `test_decorator_usage.py` - Unit tests for the code using the decorator

## Requirements

- Python 3.12+
- pytest
- pytest-mock

## Setup

This repo uses poetry 1.8.x

## Running Tests

```bash
# Run all tests
pytest

# Run tests with verbose output
pytest -v

# Run specific test file
pytest test_decorator.py
```

## License

MIT

# Understanding the `repeat_thrice` Decorator Test

## Test Overview

This test verifies that our `repeat_thrice` decorator correctly repeats the decorated function 3 times while preserving function arguments and returning the final result.

## Step-by-Step Explanation

### 1. Setup

```python
def test_repeat_thrice_decorator(mocker):
    """Test the repeat_thrice decorator."""
    mock_func = mocker.Mock(return_value="test_result")
```

- We create a mock function using `mocker.Mock()` (provided by pytest-mock)
- This mock function will always return `"test_result"` when called
- Using a mock allows us to track calls and arguments precisely

### 2. Apply the Decorator

```python
    decorated_func = repeat_thrice(mock_func)
```

- We apply our `repeat_thrice` decorator to the mock function
- This creates a new function that should call our mock 3 times when invoked

### 3. Execute the Decorated Function

```python
    result = decorated_func("test_arg", key="test_kwarg")
```

- We call the decorated function with a positional argument (`"test_arg"`) and a keyword argument (`key="test_kwarg"`)
- The decorator should pass these arguments to all three calls of the mock function

### 4. Verify Call Count

```python
    assert mock_func.call_count == 3
```

- We check that the mock function was called exactly 3 times
- This verifies the core functionality of our decorator

### 5. Verify Return Value

```python
    assert result == "test_result"
```

- We verify that the decorated function returns the same value as the original function
- Specifically, it should return the value from the last call to the mock function

### 6. Verify Call Arguments

```python
    expected_calls = [
        mocker.call("test_arg", key="test_kwarg"),
        mocker.call("test_arg", key="test_kwarg"),
        mocker.call("test_arg", key="test_kwarg"),
    ]
    mock_func.assert_has_calls(expected_calls)
```

- We create a list of expected calls, each with the same arguments
- `mocker.call()` creates objects representing individual function calls with their arguments
- `assert_has_calls()` verifies that the mock was called with exactly these arguments, in this order
- This confirms that our decorator preserves and correctly passes all arguments to each function call

This test comprehensively validates that our decorator functions as expected: repeating the function call 3 times, preserving all arguments, and returning the final result.
