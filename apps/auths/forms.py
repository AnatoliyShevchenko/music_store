# Django
from django.forms import (
    ModelForm,
    Form,
    PasswordInput,
    CharField,
    EmailField
)

# Local
from auths.models import CustomUser


class RegistrationForm(ModelForm):
    """Registration form for CustomUser."""
    
    password2 = CharField(
        label='Повторите пароль',
        max_length=100,
        widget=PasswordInput()
    )


    class Meta:
        model = CustomUser
        fields = (
            'email',
            'first_name',
            'last_name',
            'password'
        )
        widgets = {
            'password': PasswordInput(
                attrs={'class': 'psd'}
            ),
        }

    def save(self, commit: bool = ...) -> CustomUser:
        self.full_clean()
        return super().save(commit)


class LoginForm(Form):
    """Login form for CustomUser."""
    
    email = EmailField(
        label='Почта',
        max_length=100
    )
    password = CharField(
        label='Пароль',
        max_length=100,
        widget=PasswordInput()
    )


    class Meta:
        model = CustomUser
        fields = (
            'email',
            'password'
        )


class ProfileForm(Form):
    """Profile Form."""

    email = EmailField(
        label='Почта',
        max_length=100
    )
    first_name = CharField(
        label='Имя',
        max_length=50
    )
    last_name = CharField(
        label='Фамилия',
        max_length=50
    )


    class Meta:
        model = CustomUser
        fields = (
            'email',
            'first_name',
            'last_name'
        )