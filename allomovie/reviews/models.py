from django.db import models
from core.models import TimeStampedModel
from movies.models import Movie


class Review(TimeStampedModel):
    """
    Model review for a movie.
    """
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    grade = models.IntegerField(help_text="Enter the grade (1-5)")
    comment = models.TextField(help_text="Enter your review comment")

    def __str__(self):
        return f"{self.grade} - {self.movie.title}"
