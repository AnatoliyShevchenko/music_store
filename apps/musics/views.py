from django.shortcuts import render
from django.db.models import QuerySet
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from musics.models import (
    Music,
    Genre,
    Author
)

# Create your views here.
def main(request, *args, **kwargs):
    u: QuerySet = Music.objects.filter(
        genre=Genre.objects.get(title='Рок').id
    )
    return render(
        request=request,
        template_name='musics/home_page.html',
        context={
            'u': u
        }
    )

def music(request, *args, **kwargs):
    return render(template_name='musics/music_create_page.html', request=request, context={})

def genre(request, *args, **kwargs):
    return render(template_name='musics/genre_create_page.html', request=request, context={})

def author(request, *args, **kwargs):
    return render(template_name='musics/author_create_page.html', request=request, context={})