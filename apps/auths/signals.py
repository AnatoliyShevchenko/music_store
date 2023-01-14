from django.conf import settings
from django.core.mail import send_mail
from django.db.models.base import ModelBase
from django.db.models.signals import (
    post_save
)
from django.dispatch import receiver

from typing import Any

from auths.models import CustomUser


@receiver(
    post_save,
    sender=CustomUser
)
def post_save_player(
    sender: ModelBase,
    instance: CustomUser,
    created: bool,
    **kwargs: Any
) -> None:
    if not created:
        return

    send_mail(
        subject='Activation code',
        message=f'Your link: http://localhost:8000/activate/{instance.activation_code}/',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[
            'metallugabns@yandex.kz'
        ],
        fail_silently=False
    )
    print('something happend')