# hide_warnings
 This is a python module that can hide any annoying warning messages from external C and C++ libraries in your python project. There is a decorator called `hide_warnings` in this module, you can decorate any of your functions with this decorator, then no warning messages from external C and C++ libraries (if invoked) in your function will be printed to cmd/terminal.

## Installation

`pip install hide_warnings`

## Usage

For example, here is a function that when you run it, a warning message from external C and C++ libraries will be forcibly printed to cmd/terminal, which is very annoying, and in python normally it is hard to prevent the warning messages from non-python libraries, especially when the functions that throw out these warning messages is from a compiled C and C++ executable (which means you cannot modify the codes inside it) and you pretty much need to modify the source code and rebuild yourself to prevent these warning messages, and what's even worse is that some closed source C and C++ projects does not give out source codes for you to build.

What we want is to directly prevent the warning messages we do not want to see from external C and C++ libraries in our python projects.

```python
def func(a, b):
    function_throw_external_warnings()
    result = a + b
    return result

>>> func(1, 2)
warning: This is some warnings from some external C and C++ functions
3
```

By decorating the function with `hide_warnings`, you can prevent these warning messages.

```python
from hide_warnings import hide_warnings

@hide_warnings
def func(a, b):
    function_throw_external_warnings()
    result = a + b
    return result

>>> func(1, 2)
3
```

Note that by default, all of the printed messages will be prevented inside the function you are decorated, including python's own `print` functions. If you still want to use python's `print` function to print some messages that is useful to you, you can set the keyword argument `out` to `False` for the decorator, which makes the function decorated could still use python's own `print` function.

```python
from hide_warnings import hide_warnings

@hide_warnings(out=False)
def func(a, b):
    function_throw_external_warnings()
    print('this is a message')
    result = a + b
    return result

>>> func(1, 2)
this is a message
3
```

