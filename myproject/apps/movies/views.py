from django.shortcuts import render
from django.urls import reverse
from django.http import Http404, HttpResponseRedirect
from .models import Movie, User


def index(request):
    latest_movies_list = Movie.objects.order_by('-pub_date')[:5]
    return render(request, 'movies/list.html', {'latest_movies_list': latest_movies_list})


def detail(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
    except:
        raise Http404('Фильм не найден!')

    return render(request, 'movies/detail.html', {'movie': movie})


def comment(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
    except:
        raise Http404('Фильм не найден!')
    
    movie.user_set.create(name=request.POST['name'], surname=request.POST['text'])

    return HttpResponseRedirect(reverse('movies:detail'), args=(movie.id,))