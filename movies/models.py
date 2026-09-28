from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Movie(models.Model):

    class Status(models.TextChoices):
        WANT_TO_WATCH = 'want_to_watch', 'Baxmaq istəyirəm'
        WATCHING = 'watching', 'Baxıram'
        WATCHED = 'watched', 'Baxmışam'

    title = models.CharField(max_length=150)
    genre = models.CharField(max_length=100)
    release_year = models.PositiveIntegerField()

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.WANT_TO_WATCH,
    )

    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='movies',
    )

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
        ordering = ('-created_at',)

    def __str__(self):
        return f"{self.title} ({self.release_year})"
