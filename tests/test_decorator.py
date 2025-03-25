import pytest
from custom_decorator_test.decorator import repeat_thrice


def test_repeat_thrice_decorator(mocker):
    """Test the repeat_thrice decorator."""
    mock_func = mocker.Mock(return_value="test_result")

    decorated_func = repeat_thrice(mock_func)
    result = decorated_func("test_arg", key="test_kwarg")

    assert mock_func.call_count == 3
    assert result == "test_result"

    expected_calls = [
        mocker.call("test_arg", key="test_kwarg"),
        mocker.call("test_arg", key="test_kwarg"),
        mocker.call("test_arg", key="test_kwarg"),
    ]
    mock_func.assert_has_calls(expected_calls)
