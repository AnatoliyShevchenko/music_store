from django.shortcuts import render
from django.db.models import QuerySet
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.http import (
    HttpRequest,
    HttpResponse,
    QueryDict   
)
from django.views.generic import (
    View,
    ListView,
)

from musics.models import (
    Music,
    Genre,
    Author
)

from typing import Any


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


class MusicView(View):
    """View special for music model."""

    def get(self, request: HttpRequest, *args, **kwargs):
        status: list[tuple] = Music.STATUS_PATTERN
        genres = Genre.objects.all()
        authors = Author.objects.all()
        return render(
            request=request,
            template_name='musics/music_create_page.html',
            context={
                'ctx_status' : status,
                'ctx_genres' : genres,
                'ctx_authors' : authors,
            }
        )

    def post(
        self, 
        request: HttpRequest,
        *args: tuple, 
        **kwargs: dict
    ) -> HttpResponse:
        data: QueryDict = request.POST
        # breakpoint()
        title = data.get('title')
        duration = data.get('duration')
        status = data.get('status')
        genres_id: list = data.getlist('genre')
        author = data.get('author')
        music: Music = Music.objects.create(
            title=title,
            duration=duration,
            status=status,
            author_id=author,
        )
        genres: QuerySet[Genre] =\
            Genre.objects.filter(id__in=genres_id)
        music.genre.set(genres)

        return HttpResponse("Ok")

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
