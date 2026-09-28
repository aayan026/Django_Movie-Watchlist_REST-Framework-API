from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render

from .forms import MovieForm
from .models import Movie


@login_required
def movies_list(request: HttpRequest) -> HttpResponse:
    movies = Movie.objects.filter(owner=request.user)

    status = request.GET.get('status')
    genre = request.GET.get('genre')

    if status:
        movies = movies.filter(status=status)

    if genre:
        movies = movies.filter(genre__iexact=genre.strip())

    context = {
        'movies': movies,
        'status_choices': Movie.Status.choices,
        'genres': (
            Movie.objects.filter(owner=request.user)
            .order_by('genre')
            .values_list('genre', flat=True)
            .distinct()
        ),
        'selected_status': status or '',
        'selected_genre': genre or '',
    }
    return render(request, 'movies/movies_list.html', context)


@login_required
def movie_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.owner = request.user
            movie.save()
            messages.success(request, 'Film uğurla əlavə olundu')
            return redirect('movies:movies_list')
    else:
        form = MovieForm()

    return render(request, 'movies/movie_create.html', {
        'form': form,
        'mode': 'create',
    })


@login_required
def movie_edit(request: HttpRequest, movie_id: int) -> HttpResponse:
    movie = get_object_or_404(Movie, pk=movie_id)

    if movie.owner != request.user:
        return HttpResponseForbidden("Siz ancaq öz filmlərinizi dəyişə bilərsiniz")

    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            messages.success(request, 'Film uğurla yeniləndi')
            return redirect('movies:movies_list')
    else:
        form = MovieForm(instance=movie)

    return render(request, 'movies/movie_edit.html', {
        'form': form,
        'movie': movie,
        'mode': 'edit',
    })


@login_required
def movie_delete(request: HttpRequest, movie_id: int) -> HttpResponse:
    movie = get_object_or_404(Movie, pk=movie_id)

    if movie.owner != request.user:
        return HttpResponseForbidden("Siz ancaq öz filmlərinizi silə bilərsiniz")

    if request.method == 'POST':
        movie.delete()
        messages.success(request, 'Film uğurla silindi')
        return redirect('movies:movies_list')

    return render(request, 'movies/movie_delete.html', {'movie': movie})
