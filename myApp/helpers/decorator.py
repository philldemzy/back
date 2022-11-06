from functools import wraps


def my_csrf(view):
    """
    You know how decorators work now boy
    """
    @wraps(view)
    def wrapper(request, *args, **kwargs):
        view_func = view(request, *args, **kwargs)
        return view_func
    return wrapper
