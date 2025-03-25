import requests
from custom_decorator_test import decorator


@decorator.repeat_thrice
def get_chuck_norris_joke():
    """
    Fetches a random Chuck Norris joke from the public API.

    Returns:
        dict: The JSON response from the API containing the joke
    """
    url = "https://api.chucknorris.io/jokes/random"

    response = requests.get(url)
    joke_data = response.json()
    print(f"Random Chuck Norris joke: {joke_data['value']}")

    return joke_data


if __name__ == "__main__":
    get_chuck_norris_joke()
