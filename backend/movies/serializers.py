from rest_framework import serializers
from .models import Actor, Movie
from reviews.serializers import ReviewSerializer


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True,  required=False)
    reviews = ReviewSerializer(many=True, read_only=True)
    averageRating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'actors', 'reviews', 'averageRating']

    def get_averageRating(self, obj):
        return obj.average_rating()

    def create(self, validated_data):
        actors_data = validated_data.pop('actors', [])
        movie = Movie.objects.create(**validated_data)

        for actor_data in actors_data:
            actor, created = Actor.objects.get_or_create(**actor_data)
            movie.actors.add(actor)
        return movie

    def update(self, instance, validated_data):
        actors_data = validated_data.pop('actors', [])

        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.save()

        instance.actors.clear()
        for actor_data in actors_data:
            actor, created = Actor.objects.get_or_create(**actor_data)
            instance.actors.add(actor)

        return instance
