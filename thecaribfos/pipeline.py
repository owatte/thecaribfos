from django.conf import settings
from django.shortcuts import redirect
from django.contrib import messages


def prevent_dupes(backend, uid, user=None, *args, **kwargs):
    email = kwargs.get("details", {}).get("email")
    if email:
        if settings.AUTH_USER_MODEL.objects.filter(email=email).exists() and user is None:
            messages.warning(
                kwargs.get("request"),
                "It appears you already have an account on this site using another social account."
            )
            return redirect("home")
    return {}
