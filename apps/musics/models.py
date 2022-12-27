from django.db import models
from django.contrib.auth.models import User
from abstracts.models import AbstractModel

# Create your models here.
class Author(AbstractModel):
    """User but will push music for three hudred baks."""

    id = models.IntegerField(
        serialize=True,
        verbose_name='author_id',
        primary_key=True
    )
    datestart_subscribe = models.DateField(
        verbose_name="Начало подписки",
        auto_now_add=True,
    )
    followers = models.ManyToManyField(
        to=User,
        related_name='follower',
        verbose_name='подписчики',
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='пользователь',
    )

    class Meta:
        ordering = (
            '-datetime_created',
            )
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self) -> str:
        return self.user.username


class Genre(AbstractModel):
    """Model Genre"""

    id = models.IntegerField(
        serialize=True,
        verbose_name='genre_id',
        primary_key=True
    )
    title = models.CharField(
        verbose_name='Жанр',
        max_length=50,
    )

    class Meta:
        ordering = (
            '-id',
        )
        verbose_name='Жанр'
        verbose_name_plural='Жанры'

    def __str__(self) -> str:
        return self.title


class Music(AbstractModel):
    """Model Music"""

    id = models.IntegerField(
        serialize=True,
        verbose_name='music_id',
        primary_key=True,
    )
    title = models.CharField(
        verbose_name='Название',
        max_length=50,
    )
    duration = models.TimeField(
        verbose_name='длительность'
    )
    author_id = models.ForeignKey(
        Author,
        on_delete=models.PROTECT,
        null=False,
        blank=False,
    )
    genre_id = models.ForeignKey(
        Genre,
        on_delete=models.PROTECT,
        null=False,
        blank=False,
    )

    class Meta:
        ordering = (
            '-author_id',
        )
        verbose_name = 'песня'
        verbose_name_plural = 'песни'

    def __str__(self) -> str:
        return self.title