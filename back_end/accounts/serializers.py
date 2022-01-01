from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movie


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'password', 'like_movies', 'review_set',)
        read_only_fields = ('like_movies', 'review_set',)

