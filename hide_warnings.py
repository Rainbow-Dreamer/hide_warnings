import py
import py._io
import py._io.capture
import functools


def hide_warnings(function=None, out=True, in_=False):
    def decorator_hide_warnings(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                capture = py.io.StdCaptureFD(out=out, in_=in_)
            except:
                pass
            result = func(*args, **kwargs)
            try:
                capture.reset()
            except:
                pass
            return result

        return wrapper

    if function:
        return decorator_hide_warnings(function)
    return decorator_hide_warnings
