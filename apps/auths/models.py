from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.core.exceptions import ValidationError

import os

from abstracts.models import AbstractModel

# Create your models here.
class CustomUserManager(BaseUserManager):
    """ClientManager."""

    def create_user(
        self,
        email: str,
        password: str
    ) -> 'CustomUser':

        if not email:
            raise ValidationError('Email required')

        custom_user: 'CustomUser' = self.model(
            email=self.normalize_email(email),
            password=password
        )
        custom_user.set_password(password)
        custom_user.save(using=self._db)
        return custom_user

    def create_superuser(
        self,
        email: str,
        password: str,
    ) -> 'CustomUser':

        custom_user: 'CustomUser' = self.model(
            email=self.normalize_email(email),
            password=password,
        )
        custom_user.is_staff = True
        custom_user.is_superuser = True
        custom_user.set_password(password)
        custom_user.save(using=self._db)
        return

    def create_test_user(self, email, password) -> 'CustomUser':

        custom_user: 'CustomUser' = self.model(
            email=self.normalize_email(email),
            password=password
        )
        custom_user.set_password(password)
        custom_user.save(using=self._db)
        return custom_user


class CustomUser(
    AbstractBaseUser, 
    PermissionsMixin,
    AbstractModel
):
    """My custom user."""

    email = models.EmailField(
        verbose_name='email',
        unique=True
    )
    first_name = models.CharField(
        verbose_name='firstname',
        max_length=60,
        null=True,
        blank=True
    )
    last_name = models.CharField(
        verbose_name='lastname',
        max_length=70,
        null=True,
        blank=True
    )
    is_staff = models.BooleanField(
        verbose_name='staff',
        default=False
    )
    is_superuser = models.BooleanField(
        verbose_name='superuser',
        default=False
    )
    is_active = models.BooleanField(
        verbose_name='active',
        default=True
    )
    activation_code = models.CharField(
        verbose_name='code',
        max_length=40,
        null=True,
        blank=True
    )
    avatar = models.ImageField(
        verbose_name='аватарка',
        upload_to='images/',
        default=''
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        ordering = ('-datetime_created',)
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self) -> str:
        return self.first_name

    # def save(self, *args: tuple, **kwargs: dict) -> None:
    #     self.full_clean()
    #     code: str = os.urandom(20).hex()
        
    #     self.activation_code = code
    #     return super().save(*args, **kwargs)