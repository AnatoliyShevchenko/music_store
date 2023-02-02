from django.db import models
from django.db.models import QuerySet
from django.contrib.auth.models import User

from abstracts.models import AbstractModel, AbstractManager
from auths.models import CustomUser

# Create your models here.
class AuthorManager(AbstractManager):
    """Manager for author"""

    def get_music_by_user(self, user: str) -> QuerySet['Music']:
        id: str =\
            Author.objects.get(user=user).id
        return self.filter(
            author=id
        )
    
    def get_music_by_first_name(self, first_name: str) -> QuerySet['Music']:
        id: str =\
            Author.objects.get(first_name=first_name).id
        return self.filter(
            author=id
        )

    def get_music_by_last_name(self, last_name: str) -> QuerySet['Music']:
        id: str =\
            Author.objects.get(last_name=last_name).id
        return self.filter(
            author=id
        )

class Author(AbstractModel):
    """User but will push music for three hundred baks."""

    datestart_subscribe = models.DateField(
        verbose_name="Начало подписки",
        auto_now_add=True,
    )
    followers = models.ManyToManyField(
        to=CustomUser,
        related_name='follower',
        verbose_name='подписчики',
    )
    user = models.ForeignKey(
        to=CustomUser,
        on_delete=models.CASCADE,
        verbose_name='пользователь',
    )
    title = models.CharField(
        max_length=30,
        verbose_name='Исполнитель',
        unique=True
    )

    class Meta:
        ordering = (
            '-datetime_created',
            )
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self) -> str:
        return self.title


class Genre(AbstractModel):
    """Model Genre"""

    title = models.CharField(
        verbose_name='Жанр',
        max_length=50,
        unique=True,
    )

    class Meta:
        ordering = (
            '-title',
        )
        verbose_name='Жанр'
        verbose_name_plural='Жанры'

    def __str__(self) -> str:
        return self.title


class MusicManager(AbstractManager):
    """Manager special for Music."""

    def get_music_by_genre(self, title: str) -> QuerySet['Music']:
            id: str =\
                Genre.objects.get(title=title).id
            return self.filter(
                genre=id
            )

    def get_music_by_status(self, status: str) -> QuerySet['Music']:
        title: str =\
            Music.objects.get(status=status).title
        return self.filter(
            music=title
        )


class Music(AbstractModel):
    """Model Music"""

    STATUS_PATTERN = (
        ('BR', 'Предрелиз'),
        ('R', 'Релиз'),
        ('AR', 'Unknown')
    )
    title = models.CharField(
        verbose_name='Название',
        max_length=50,
    )
    duration = models.TimeField(
        verbose_name='длительность',
    )
    author = models.ForeignKey(
        to=Author,
        on_delete=models.CASCADE,
        verbose_name='исполнитель',
    )
    genre = models.ManyToManyField(
        to=Genre,
        verbose_name='жанры'
    )
    status = models.CharField(
        verbose_name='статус',
        choices=STATUS_PATTERN,
        default='Unknown',
        max_length=100
    )
    image = models.ImageField(
        verbose_name='изображение',
        upload_to='images/',
        default=''
    )

    class Meta:
        ordering = (
            '-datetime_created',
        )
        verbose_name = 'трек'
        verbose_name_plural = 'треки'

    def __str__(self) -> str:
        return self.title