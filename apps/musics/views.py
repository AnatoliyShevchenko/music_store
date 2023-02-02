from django.shortcuts import render
from django.db.models import QuerySet
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.http import (
    HttpRequest,
    HttpResponse,
    QueryDict,
    JsonResponse,   
)
from django.views.generic import (
    View,
)
from django import forms
from django.core.files.uploadedfile import InMemoryUploadedFile

from musics.models import (
    Music,
    Genre,
    Author
)
from abstracts.mixins import HttpResponseMixin
from musics.forms import TempForm, RegForm, MusicForm
from auths.models import CustomUserManager

from typing import Any
import os


class MainView(View):
    """Main view."""

    queryset: QuerySet = Music.objects.all()

    def get(self, request: HttpRequest, *args, **kwargs):
        u: QuerySet
        try:
            u = Music.objects.filter(
                genre=Genre.objects.get(title='Industrial').id
            )
        except:
            u = {}

        return render(
            request=request,
            template_name='musics/home_page.html',
            context={
                'u': u
            }
        )


class MusicView(HttpResponseMixin, View):
    """View special for music model."""

    form = MusicForm

    def get(self, request: HttpRequest, *args, **kwargs):
        return self.get_http_response(
            request=request,
            template_name='musics/temp.html',
            context={
                'ctx_form' : self.form()
            }
        )

    def post(
        self, 
        request: HttpRequest,
        *args: tuple, 
        **kwargs: dict
    ) -> HttpResponse:
        images: InMemoryUploadedFile = request.FILES.get('image')
        images.name = os.urandom(20).hex().join('.jpg')
        form = self.form(
            request.POST,
            request.FILES
        )
        if not form.is_valid():
            return HttpResponse('Bad')
        print(form.cleaned_data)
        form.save()
        return HttpResponse('OK')


class GenreView(View):
    """View special for music model."""

    def get(self, request: HttpRequest, *args, **kwargs):
        titles: list[tuple] = Genre.objects.all()
        return render(
            request=request,
            template_name='musics/genre_create_page.html',
            context={
                'ctx_titles' : titles,
            }
        )


class AuthorView(View):
    """View special for music model."""

    def get(self, request: HttpRequest, *args, **kwargs):
        titles: list[tuple] = Author.objects.all()
        return render(
            request=request,
            template_name='musics/author_create_page.html',
            context={
                'ctx_titles' : titles,
            }
        )


class TempView(HttpResponseMixin, View):
    """Temp, Delete later."""

    form = TempForm

    def get(
        self, 
        request: HttpRequest, 
        *args, 
        **kwargs
    ) -> HttpResponse:
        return self.get_http_response(
            request=request,
            template_name='musics/temp.html',
            context={'ctx_form' : self.form()}
        )

    def post(
        self, 
        request: HttpRequest,
        *args: tuple, 
        **kwargs: dict
    ) -> HttpResponse:
        form = self.form(request.POST or None)
        return HttpResponse('Ok')


class RegView(HttpResponseMixin, View):
    """RegistrationView"""

    form = RegForm

    def get(
        self, 
        request: HttpRequest, 
        *args, 
        **kwargs
    ) -> HttpResponse:
        return self.get_http_response(
            request=request,
            template_name='musics/reg.html',
            context={'ctx_form' : self.form()}
        )

    def post(
        self, 
        request: HttpRequest,
        *args: tuple, 
        **kwargs: dict
    ) -> HttpResponse:
        form = self.form(request.POST or None)
        if not form.is_valid():
            return HttpResponse('Bad')
        print(form.cleaned_data)
        form.save()
        return HttpResponse('OK')