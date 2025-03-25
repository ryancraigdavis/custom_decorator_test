import pytest
from custom_decorator_test.decorator_usage import get_chuck_norris_joke


def test_get_chuck_norris_joke_core_functionality(mocker):
    """Test get_chuck_norris_joke function without the decorator."""
    mock_response = mocker.Mock()
    mock_response.json.return_value = {
        "value": "Chuck Norris counted to infinity. Twice.",
        "id": "abc123",
        "url": "https://api.chucknorris.io/jokes/abc123",
    }

    mocked_requests_get = mocker.patch("requests.get", return_value=mock_response)

    # Call the function without the decorator, the type: ignore is needed because the type checker doesnt know that the __wrapped__ attribute exists
    wrapped_get_chuck_norris_joke = get_chuck_norris_joke.__wrapped__  # type: ignore
    actual_result = wrapped_get_chuck_norris_joke()

    mocked_requests_get.assert_called_once_with(
        "https://api.chucknorris.io/jokes/random"
    )
    mock_response.json.assert_called_once()

    assert actual_result == {
        "value": "Chuck Norris counted to infinity. Twice.",
        "id": "abc123",
        "url": "https://api.chucknorris.io/jokes/abc123",
    }
    mocked_requests_get.assert_called_once_with(
        "https://api.chucknorris.io/jokes/random"
    )
