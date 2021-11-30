import py
import py._io
import py._io.capture
import functools


def get_capture(out, in_):
    try:
        capture = py.io.StdCaptureFD(out=out, in_=in_)
    except:
        capture = None
    return capture


def reset_capture(capture):
    if capture is not None:
        capture.reset()


def hide_warnings(function=None, out=True, in_=False):
    def decorator_hide_warnings(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            capture = get_capture(out, in_)
            result = func(*args, **kwargs)
            reset_capture(capture)
            return result

        return wrapper

    if function:
        return decorator_hide_warnings(function)
    return decorator_hide_warnings
