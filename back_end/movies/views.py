from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MovieListSerializer, MovieSerializer, ReviewListSerializer, ReviewSerializer, CommentListSerializer, CommentSerializer
from django.db.models import Count
from .models import Review, Movie, Comment
from django.http.response import JsonResponse
from rest_framework import status
from datetime import datetime
import random
from django.db.models import Q
import heapq
from django.db.models.aggregates import Avg


# Create your views here.
@api_view(['GET'])
def index(request):
    if request.method == 'GET':
        latest_movies = Movie.objects.order_by('-release_date')[:15]
        serializer1 = MovieListSerializer(latest_movies, many=True)

        now_month = datetime.now().month
        if now_month % 11 < 2:
            season_movies = Movie.objects.filter(Q(overview__contains='크리스마스') | Q(title__contains='겨울') | Q(overview__contains='빙하'))
        elif now_month % 11 < 5:
            season_movies = Movie.objects.filter(Q(overview__contains='사랑') | Q(overview__contains='봄'))
        elif now_month % 11 < 8:
            season_movies = Movie.objects.filter(Q(overview__contains='공포') | Q(overview__contains='여름') | Q(overview__contains='휴가'))
        else:
            season_movies = Movie.objects.filter(Q(overview__contains='우주') | Q(overview__contains='탐험'))

        season_movies_ids = list(season_movies.values_list('id', flat=True))
        random_season_movies = Movie.objects.filter(id__in=season_movies_ids)
        serializer2 = MovieListSerializer(random_season_movies, many=True)

        like_movies = Movie.objects.annotate(count=Count('like_users')).order_by('-count')[:15]
        serializer3 = MovieListSerializer(like_movies, many=True)

        movie_ids = list(Movie.objects.values_list('id', flat=True))
        rand_ids = random.sample(movie_ids, 5)
        random_movies = Movie.objects.filter(id__in=rand_ids)

        # User-User
        other_reviews = []  # 사용자가 본 영화에 달린 다른 사용자의 리뷰
        watched_movie_ids = []  # 사용자가 본 모든 영화
        check_user_ids = set() # 유사성을 확인할 모든 유저
        suggested_movie_data = []  # 유사성, 영화 번호 순의 데이터
        suggested_movie_ids = []  # 맞춤형 추천 영화의 ID

        user_reviews = Review.objects.filter(user_id=request.user.pk)
        if user_reviews:
            # 로그인된 사용자가 작성한 리뷰의 평점 평균
            user_average = user_reviews.aggregate(Avg('rank')).get('rank__avg')

        for user_review in user_reviews:
            # 유저가 이미 본 영화 제외
            watched_movie_ids.append(user_review.movie_id)
            if user_review.rank >= user_average + 0.5:  # 자신의 평균보다 0.5점 이상 높게 준 영화에 대해
                # 해당 영화의 다른 리뷰 가져오기
                other_reviews.extend(Review.objects.filter(movie_id=user_review.movie_id).exclude(user_id=request.user.pk))

        for other_review in other_reviews:
            check_user_ids.add(other_review.user_id)

        check_user_ids = random.sample(list(check_user_ids), min(20, len(check_user_ids)))

        for check_user_id in check_user_ids:
            user_similarity = 0
            check_user_reviews = Review.objects.filter(user_id=check_user_id)  # 비교할 사용자의 모든 리뷰
            check_user_average = check_user_reviews.aggregate(Avg('rank')).get('rank__avg')  # 비교할 사용자의 평점 평균

            for check_user_review in check_user_reviews:
                # 사용자가 본 영화
                if check_user_review.movie_id in watched_movie_ids:
                    # 평균 대비 영화 평점
                    user_review_dev = user_average - Review.objects.get(user_id=request.user.pk, movie_id=check_user_review.movie_id).rank 
                    check_user_review_dev = check_user_average - check_user_review.rank
                    dev_diff = abs(user_review_dev - check_user_review_dev)
                
                    if dev_diff <= 2:
                        user_similarity += (3 - dev_diff) ** 2
                    else:
                        user_similarity -= dev_diff
            
            if user_similarity > 0:
                for check_user_review in check_user_reviews:
                    if check_user_review.movie_id not in watched_movie_ids\
                        and check_user_review.rank > check_user_average:
                        heapq.heappush(suggested_movie_data, (-user_similarity, check_user_review.movie_id))
    
        if len(suggested_movie_data) > 0: 
            for idx in range(len(suggested_movie_data)):
                suggested_movie_ids.append(suggested_movie_data[idx][1])
            suggestions = min(5, len(suggested_movie_ids))
            suggested_movie_ids = suggested_movie_ids[:suggestions]
            suggested_movies = Movie.objects.filter(id__in=suggested_movie_ids) 
        else:
            suggested_movies = random_movies

        serializer4 = MovieListSerializer(suggested_movies, many=True)

        now_month = datetime.now().month
        now_day = datetime.now().day

        if len(str(now_month)) <= 1:
            now_month = "0" + str(now_month)

        if len(str(now_day)) <= 1:
            now_day = "0" + str(now_day)
        
        today = str(now_month) + "-" + str(now_day)

        today_movie = Movie.objects.filter(release_date__icontains=today)

        serializer5 = MovieSerializer(today_movie, many=True)

        return Response([serializer1.data, serializer2.data, serializer3.data, serializer4.data, serializer5.data])


@api_view(['GET'])
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['POST'])
def likes(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if movie.like_users.filter(pk=request.user.pk).exists():
        movie.like_users.remove(request.user)
        liked = False
    else:
        movie.like_users.add(request.user)
        liked = True
    context = {
        'liked': liked,
        'count': movie.like_users.count(),
    }
    return JsonResponse(context)


@api_view(['POST'])
def search(request):
    query = request.data.get('input_data')
    if query.strip():
        found_movies = Movie.objects.filter(
            Q(title__icontains=query) | Q(title__icontains=query.replace(" ", "")) |
            Q(overview__icontains=query)
        ).order_by('-release_date')
    else:
        found_movies = Movie.objects.none()
    serializer = MovieSerializer(found_movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def review_list(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    reviews = movie.review_set.all()
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def review_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = ReviewListSerializer(review)
    return Response(serializer.data)


@api_view(['DELETE'])
def review_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.user == review.user:
        if request.method == 'DELETE':
            review.delete()
            return Response({'data': '삭제되었습니다.'}, status=status.HTTP_204_NO_CONTENT)
    return Response({'error': '권한이 없습니다.'})


@api_view(['GET'])
def comment_list(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comments = review.comment_set.all()
    serializer = CommentListSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def comment_create(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(review=review, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
def comment_delete(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user == comment.user:
        if request.method == 'DELETE':
            comment.delete()
            return Response({'data': '삭제되었습니다.'}, status=status.HTTP_204_NO_CONTENT)
    return Response({'error': '권한이 없습니다.'})