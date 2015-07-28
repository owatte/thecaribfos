# -*- coding: utf-8 -*-
from functools import wraps

from django.http import Http404
from django.shortcuts import get_object_or_404
from django.utils.decorators import available_attrs

def ownership_required(function, model='', owner_field='owner', slug_field='slug'):
    u"""Check if current user is the object's owner)

    This decorator is active for views where profile is required.
    If the user profile is empty, user is redirect to the profile form.

    Use it after decorator login_required
    """
    def decorator(view_func):
        @wraps(view_func, assigned=available_attrs(view_func))
        def _wrapped_view(request, *args, **kwargs):
            current_object = get_object_or_404(model, slug=kwargs.get(slug_field))
            if getattr(current_object, owner_field) != request.user:
                raise Http404
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    if function:
        return decorator(function)
    else:
        return decorator
