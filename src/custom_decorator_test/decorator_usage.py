import requests
from custom_decorator_test import decorator


@decorator.repeat_thrice
def get_chuck_norris_joke():
    """Simple function to test the repeat_thrice_func_tools decorator."""
    url = "https://api.chucknorris.io/jokes/random"

    response = requests.get(url)
    joke_data = response.json()
    print(f"Random Chuck Norris joke: {joke_data['value']}")

    return joke_data


if __name__ == "__main__":
    get_chuck_norris_joke()
