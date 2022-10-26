from functools import wraps
from pickle import loads

from django.http import JsonResponse


def my_csrf(view):
    """
    You know how decorators work now boy
    """
    @wraps(view)
    def wrapper(request, *args, **kwargs):
        view_func = view(request, *args, **kwargs)
        return view_func
    return wrapper
