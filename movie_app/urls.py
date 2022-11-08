from . import views
from django.urls import path

urlpatterns = [
    path('', views.show_all_movie),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='movie-detail'),
    path('actors/', views.show_all_actors),
    path('actors/actor', views.show_one_actor),
    path('director/', views.show_all_directors),
    path('director/', views.show_one_director),
]
