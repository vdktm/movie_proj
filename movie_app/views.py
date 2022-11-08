from django.shortcuts import render, get_object_or_404
from .models import Movie
from django.db.models import F


def show_all_movie(request):
    movies = Movie.objects.order_by(F('year').asc(nulls_last=True), 'rating')
    return render(request, 'movie_app/all_movies.html', {
        'movies': movies
    })


def show_one_movie(request, slug_movie: str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {
        'movie': movie
    })


def show_all_actors(request):
    return render(request, 'movie_app/all_actors.html')


def show_one_actor(request):
    return render(request, 'movie_app/one_actor.html')


def show_all_directors(request):
    return render(request, 'movie_app/all_directors.html')


def show_one_director(request):
    return render(request, 'movie_app/one_director.html')
