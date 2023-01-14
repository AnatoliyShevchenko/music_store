from django.db import models
from django.db.models import QuerySet
from django.utils import timezone

# Create your models here.
class AbstractQuerySet(models.QuerySet):
    """Pre-setup QuerySet for AbstractManager."""

    def delete(self, *args, **kwargs) -> None:
        self.update(
            datetime_deleted=timezone.now()
        )


class AbstractManager(models.Manager):
    """Manager for AbstractModel class."""

    def get_not_deleted(self) -> QuerySet:
        return self.filter(
            datetime_deleted__isnull=True
        )

    def get_deleted(self) -> QuerySet:
        return self.filter(
            datetime_deleted__isnull=False
        )

    def get_queryset(self) -> QuerySet['AbstractQuerySet']:
        return AbstractQuerySet(
            self.model,
            using=self._db
        )


class AbstractModel(models.Model):
    """Abstract model for description all custom models."""

    datetime_created = models.DateTimeField(
        verbose_name="Время создания",
        auto_now_add=True,
    )
    datetime_updated = models.DateTimeField(
        verbose_name="Время обновления",
        auto_now=True,
    )
    datetime_deleted = models.DateTimeField(
        verbose_name="Время удаления",
        null=True,
        blank=True,
    )
    objects = AbstractManager()

    class Meta:
        abstract = True