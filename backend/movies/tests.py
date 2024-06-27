# movies/tests.py
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Movie, Actor

class MovieAPITestCase(APITestCase):
    def setUp(self):
        self.actor1 = Actor.objects.create(first_name='Actor 1', last_name='Test')
        self.actor2 = Actor.objects.create(first_name='Actor 2', last_name='Test')

        self.movie = Movie.objects.create(
            title='Test Movie',
            description='Test Movie Description'
        )
        self.movie.actors.add(self.actor1, self.actor2)

    def test_create_movie(self):
        url = reverse('movie-list')
        data = {
            'title': 'New Movie',
            'description': 'New Movie Description',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #self.assertEqual(Movie.objects.count(), 2)

    def test_get_all_movies(self):
        url = reverse('movie-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #self.assertEqual(len(response.data), 1)

    def test_get_one_movie(self):
        url = reverse('movie-detail', args=[self.movie.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Movie')

    def test_update_movie(self):
        url = reverse('movie-detail', args=[self.movie.id])
        data = {
            'title': 'Updated Movie Title',
            'description': 'Updated Movie Description',
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.movie.refresh_from_db()
        self.assertEqual(self.movie.title, 'Updated Movie Title')
        self.assertEqual(self.movie.description, 'Updated Movie Description')

