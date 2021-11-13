import py
import functools


def hide_warnings(function=None, out=True, in_=False):
    def decorator_hide_warnings(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            capture = py.io.StdCaptureFD(out=out, in_=in_)
            result = func(*args, **kwargs)
            capture.reset()
            return result

        return wrapper

    if function:
        return decorator_hide_warnings(function)
    return decorator_hide_warnings
