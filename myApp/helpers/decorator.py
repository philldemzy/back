from functools import wraps

from django.http import JsonResponse


def my_csrf(view):
    """
    This decorator checks against csrf attacks
    I will be storing the token in the session file
    and cross-checking them here.
    """
    @wraps(view)
    def wrapper(request, *args, **kwargs):
        if request.method == "POST":
            token = request.headers.get('x-token')  # check for token in request header
            if not token:
                return JsonResponse({'forbidden': 'token not set'}, status=403)  # if no token return
            if token in request.session:
                view_func = view(request, *args, **kwargs)  # run view function only if token is present
                request.session.pop(token)  # remove token after function has ran
                return view_func
            return JsonResponse({'forbidden': 'action is not allowed'}, status=403)
        return view(request, *args, **kwargs)  # go to view as it is not a post request
    return wrapper
