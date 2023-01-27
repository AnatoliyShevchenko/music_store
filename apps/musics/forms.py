from django import forms

from musics.models import Music
from auths.models import CustomUser


class TempForm(forms.Form):
    """TempForm."""

    title = forms.CharField(
        max_length=100,
        label='Заголовок'
    )
    duration = forms.TimeField(
        required=True,
        label='Длительность',
        widget=forms.TimeInput(
            attrs={
                'type' : 'time'
            })
    )
    description = forms.CharField(
        max_length=100,
        widget=forms.Textarea(
            attrs={
                'class' : 'temp'
            }
        ),
        label='Описание'
    )


class RegForm(forms.ModelForm):
    """Registration"""

    password = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                'type' : 'password'
            }
        )
    )
    # retry_password = forms.CharField(
    #     max_length=50,
    #     widget=forms.PasswordInput(
    #         attrs={
    #             'type' : 'password'
    #         }
    #     )
    # )

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name']


class MusicForm(forms.ModelForm):
    """MusicForm"""

    class Meta:
        model = Music
        fields = '__all__'
        widgets = {'duration' : forms.TimeInput(
            attrs={'type' : 'time'}
        )}