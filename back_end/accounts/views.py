from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from movies.models import Movie
from movies.serializers import MovieListSerializer, ReviewListSerializer
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404


@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
	# 1-1. Client에서 온 데이터를 받아서
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
	# 1-2. 패스워드 일치 여부 체크
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
    if len(password) < 8:
        return Response({'pass_error': '비밀번호는 8글자 이상이어야 합니다.'}, status=status.HTTP_400_BAD_REQUEST)
	# 2. UserSerializer를 통해 데이터 직렬화
    serializer = UserSerializer(data=request.data)
	# 3. validation 작업 진행 -> password도 같이 직렬화 진행
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        #4. 비밀번호 해싱 후 
        user.set_password(request.data.get('password'))
        user.save()
        # password는 직렬화 과정에는 포함 되지만 → 표현(response)할 때는 나타나지 않는다. (write_only)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def profile(request):
    person = get_object_or_404(get_user_model(), pk=request.user.pk)
    movies = person.like_movies.all()
    serializer1 = MovieListSerializer(movies, many=True)
    
    reviews = person.review_set.all()
    serializer2 = ReviewListSerializer(reviews, many=True)

    like_movies = person.like_movies.all()
    genre_list = []
    max_count = []
    for like_movie in like_movies:
        genre_list.append(like_movie.genre)

    for list in genre_list:
        max_count.append([(genre_list.count(list)), list])

    if len(max_count) != 0:
        max_genre = max(max_count)[1]
        max_genre_movies = Movie.objects.filter(genre=max_genre)[:20]
        serializer3 = MovieListSerializer(max_genre_movies, many=True)
        return Response([serializer1.data, serializer2.data, serializer3.data])
    else:
        return Response([serializer1.data, serializer2.data])