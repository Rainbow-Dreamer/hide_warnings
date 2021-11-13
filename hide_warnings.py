import py
import functools


def hide_warnings(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        capture = py.io.StdCaptureFD()
        result = func(*args, **kwargs)
        capture.reset()
        return result

    return wrapper
