from django.db import models
from django.db.models import QuerySet
from django.contrib.auth.models import User

from abstracts.models import AbstractModel, AbstractQuerySet
from auths.models import CustomUser

# Create your models here.
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

    class Meta:
        ordering = (
            '-datetime_created',
            )
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self) -> str:
        return self.user.email


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
        to='Author',
        on_delete=models.CASCADE,
        verbose_name='автор',
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

    class Meta:
        ordering = (
            '-datetime_created',
        )
        verbose_name = 'трек'
        verbose_name_plural = 'треки'

    def __str__(self) -> str:
        return self.title