from django.contrib.postgres.fields import ArrayField
from django.core.validators import DecimalValidator
from django.db import models


class Route(models.Model):

    coordinates = ArrayField(
        ArrayField(
            models.DecimalField(
                max_digits=11, decimal_places=8, blank=True, validators=[DecimalValidator]),
            size=2),
        blank=True,
        default=list,
    )
    length = models.FloatField(blank=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [models.Index(fields=['-length'])]
