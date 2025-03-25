import functools


def repeat_thrice(func):
    """A simple decorator that executes the decorated function three times."""

    def wrapper(*args, **kwargs):
        """Wrapper function that executes the decorated function three times."""
        result = None
        for _ in range(3):
            result = func(*args, **kwargs)
        print(f"Wrapper function name: {wrapper.__name__}")
        return result

    return wrapper


def repeat_thrice_func_tools(func):
    """A simple decorator that executes the decorated function three times."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper function that executes the decorated function three times."""
        result = None
        for _ in range(3):
            result = func(*args, **kwargs)
        print(f"Wrapper function name: {wrapper.__name__}")
        return result

    return wrapper
