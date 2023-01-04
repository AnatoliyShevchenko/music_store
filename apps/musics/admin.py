from django.contrib import admin
from musics.models import Author, Genre, Music
from django.core.handlers.wsgi import WSGIRequest
from typing import Optional


# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    model = Author
    list_display = [
        'datetime_created',
        'datestart_subscribe',
        'user',
    ]

    def get_readonly_fields(self, request: WSGIRequest, obj: Optional[Genre] = None):
        if not obj:
            return self.readonly_fields

        return self.readonly_fields + (
            'datetime_created',
            'followers',
            )


class GenreAdmin(admin.ModelAdmin):
    model = Genre
    list_display = [
        'title'
    ]

    # def get_readonly_fields(self, request: WSGIRequest, obj: Optional[Genre] = None):
    #     if not obj:
    #         return self.readonly_fields

    #     return self.readonly_fields + ('title')


class MusicAdmin(admin.ModelAdmin):
    model = Music
    list_display = [
        'title',
        'duration',
        'author',
        'status',
    ]

    # def get_readonly_fields(self, request: WSGIRequest, obj: Optional[Music] = None):
    #     if not obj:
    #         return self.readonly_fields

    #     return self.readonly_fields + ('title')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Music, MusicAdmin)