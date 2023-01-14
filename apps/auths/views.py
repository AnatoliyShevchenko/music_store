from django.shortcuts import render
from django.http import (
    HttpRequest, 
    HttpResponse
)
from django.db.models import QuerySet

from auths.models import CustomUser

# Create your views here.
def activate_user(
    request: HttpRequest, 
    code: str, 
    *args: tuple, 
    **kwargs: dict
    ) -> HttpResponse:
    """Check and activate user."""

    custom_user: QuerySet[CustomUser] =\
        CustomUser.objects.filter(
            activation_code=code
        )
    if custom_user:
        user: CustomUser = custom_user[0]
        if not user.is_active:
            user.is_active = True
            user.save()
            return HttpResponse('Successful')

    return HttpResponse('Bad activate!')