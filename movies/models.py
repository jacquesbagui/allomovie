from django.db import models
from allomovie.core.models import TimeStampedModel


class Actor(TimeStampedModel):
    """
    Actor Model
    """
    first_name = models.CharField(max_length=100, help_text="Enter the first name")
    last_name = models.CharField(max_length=100, help_text="Enter the last name")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Movie(TimeStampedModel):
    """
    Actor Movie
    """
    title = models.CharField(max_length=255, help_text="Enter the movie title")
    description = models.TextField(help_text="Enter the movie description")
    actors = models.ManyToManyField(Actor, help_text="Select actors for this movie")

    def __str__(self):
        return self.title
