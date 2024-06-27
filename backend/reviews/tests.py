from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from movies.models import Movie, Actor
from reviews.models import Review


class ReviewAPITestCase(TestCase):
    def setUp(self):
        self.actor = Actor.objects.create(first_name='Actor', last_name='review test')

        self.movie = Movie.objects.create(
            title='Test Movie',
            description='Test Movie Description'
        )
        self.movie.actors.add(self.actor)

        self.review = Review.objects.create(
            movie=self.movie,
            comment='Great movie!',
            grade=5
        )

    def test_get_review_list(self):
        url = reverse('review-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_review(self):
        url = reverse('review-list')
        data = {'movie': self.movie.id, 'comment': 'Another great movie!', 'grade': 4}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
