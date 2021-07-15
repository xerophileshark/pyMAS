# Standard library imports
from functools import wraps # This convenience func preserves name and docstring

# Third party imports

# Local application imports

def add_method(cls):
    """
    This function is a decorator and adds a method to a class instance.
    
    Usage:
        @add_method(class_name)
        def your_function(**args):
            pass

    """
    def decorator(func):
        @wraps(func) 
        def wrapper(self, *args, **kwargs): 
            return func(*args, **kwargs)
        setattr(cls, func.__name__, wrapper)
        # Note we are not binding func, but wrapper which accepts self but does exactly the same as func
        return func # returning func means func can still be used normally
    return decorator