def repeat_thrice(func):
    """A simple decorator that executes the decorated function three times."""

    def wrapper(*args, **kwargs):
        """Wrapper function that executes the decorated function three times."""
        result = None
        for _ in range(3):
            result = func(*args, **kwargs)
        return result

    return wrapper
