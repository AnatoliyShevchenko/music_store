from django.shortcuts import render
from django.db.models import QuerySet
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.http import (
    HttpRequest,
    HttpResponse,
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

# Create your views here.
# def main(request, *args, **kwargs):
#     u: QuerySet = Music.objects.filter(
#         genre=Genre.objects.get(title='Рок').id
#     )
#     return render(
#         request=request,
#         template_name='musics/home_page.html',
#         context={
#             'u': u
#         }
#     )

def music(request, *args, **kwargs):
    return render(template_name='musics/music_create_page.html', request=request, context={})

def genre(request, *args, **kwargs):
    return render(template_name='musics/genre_create_page.html', request=request, context={})

def author(request, *args, **kwargs):
    return render(template_name='musics/author_create_page.html', request=request, context={})


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
        return render(
            request=request,
            template_name='musics/music_create_page.html',
            context={
                'ctx_status' : status,
                'ctx_genres' : genres,
            }
        )