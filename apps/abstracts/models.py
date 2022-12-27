from django.db import models

# Create your models here.
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
    
    class Meta:
        abstract = True