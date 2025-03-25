import pytest
import requests
from custom_decorator_test.decorator_usage import get_chuck_norris_joke


# def test_get_chuck_norris_joke_core_functionality(mocker):
#     """Test get_chuck_norris_joke function with the decorator mocked out."""
#     # First, we need to patch the decorator to pass through the original function
#     # We'll need to patch the module where the decorator is applied
#     # This bypasses the decorator's effect

#     # Create a mock response
#     mock_response = mocker.Mock()
#     mock_response.json.return_value = {
#         "value": "Chuck Norris counted to infinity. Twice.",
#         "id": "abc123",
#         "url": "https://api.chucknorris.io/jokes/abc123",
#     }

#     # Patch requests.get to return our mock
#     mocked_requests_get = mocker.patch("requests.get", return_value=mock_response)

#     # Get a reference to the original function without decorator
#     # This requires getting the function from the internal wrapper if it's already decorated
#     # We can get this either by importing the function before decoration or by accessing it directly

#     # Option 1: If get_chuck_norris_joke is the decorated function, we can mock __wrapped__ to get the original
#     original_func = mocker.patch.object(
#         get_chuck_norris_joke_func_tools,
#         "__wrapped__",
#         side_effect=get_chuck_norris_joke_func_tools,
#     )

#     # Call the function (which will now call our mocked function instead of going through decorator)
#     result = get_chuck_norris_joke_func_tools()

#     # Verify the request was made correctly
#     mocked_requests_get.assert_called_once_with(
#         "https://api.chucknorris.io/jokes/random"
#     )

#     # Verify the json method was called
#     mock_response.json.assert_called_once()

#     # Verify we got the expected result
#     assert result == {
#         "value": "Chuck Norris counted to infinity. Twice.",
#         "id": "abc123",
#         "url": "https://api.chucknorris.io/jokes/abc123",
#     }

#     # Verify our function was only called once (proving decorator was bypassed)
#     assert original_func.call_count == 1
