from django.urls import path
from . import views 

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('<int:movie_pk>/likes/', views.likes, name='likes'),
    path('review_list/<int:movie_pk>/', views.review_list, name='review_list'),
    path('review_create/<int:movie_pk>/', views.review_create, name='review_create'),
    path('review_delete/<int:review_pk>/', views.review_delete, name='review_delete'),
    path('review_detail/<int:review_pk>/', views.review_detail, name='review_detail'),
    path('review/comment_create/<int:review_pk>/', views.comment_create, name='comment_create'),
    path('review/comment_delete/<int:comment_pk>/', views.comment_delete, name='comment_delete'),
    path('review/comment_list/<int:review_pk>/', views.comment_list, name='comment_list'),
]