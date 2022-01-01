from rest_framework import serializers
from .models import Movie, Review, Comment
from accounts.models import User
from accounts.serializers import UserSerializer


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fileds = ('like_users',)



class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fileds = ('like_users',)



class ReviewListSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(instance=Movie)
    user = UserSerializer(instance=User)
    
    class MovieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = ('title',)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fileds = ('user', 'movie',)


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user', 'movie',)


class CommentListSerializer(serializers.ModelSerializer):
    review = ReviewSerializer(instance=Review)
    user = UserSerializer(instance=User)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user', 'review',)


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user', 'review',)
