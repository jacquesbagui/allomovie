from rest_framework import viewsets, pagination
from .models import Actor, Movie
from .serializers import ActorSerializer, MovieSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = pagination.PageNumberPagination
