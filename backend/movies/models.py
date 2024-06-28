from django.db import models
from core.models import TimeStampedModel


class Actor(TimeStampedModel):
    """
    Actor Model
    """
    first_name = models.CharField(max_length=100, help_text="Enter the first name")
    last_name = models.CharField(max_length=100, help_text="Enter the last name", blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Movie(TimeStampedModel):
    """
    Actor Movie
    """
    title = models.CharField(max_length=255, help_text="Enter the movie title")
    description = models.TextField(help_text="Enter the movie description")
    actors = models.ManyToManyField(Actor, help_text="Select actors for this movie", blank=True)

    def __str__(self):
        return self.title

    def has_reviews(self):
        return self.reviews.exists()

    def average_rating(self):
        if self.has_reviews():
            average = sum(review.grade for review in self.reviews.all()) / self.reviews.count()
            return round(average, 2)
        return 0
