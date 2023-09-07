from django.urls import path, include
from .views import *

urlpatterns = [    
    path('',  HomeView.as_view(), name="home"),

    path('generos/',  GenderList.as_view(), name="generos"),
    path('companias/',  CompanyList.as_view(), name="companias"),

    path('movies/',  MovieList.as_view(), name="movies"),
    path('movie_create/',  MovieCreate.as_view(), name="movie-create"),
    path('movie_update/<int:pk>/',  MovieUpdate.as_view(), name="movie-update"),
    path('movie_delete/<int:pk>/',  MovieDelete.as_view(), name="movie-delete"),
]
