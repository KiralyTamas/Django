from django.shortcuts import render
from moviesapp.models import Movies
from moviesapp.forms import MoviesForm

def index(request):
    return render(request, 'moviesapp/index.html')

def moviesList(request):
    moviesList=Movies.objects.all()
    movies_dict={'movies':moviesList}
    return render(request, 'moviesapp/moviesList.html',movies_dict)

def addMovies(request):
    success=str("Successfuly Movie Registration")
    moviesForm=MoviesForm()
    movies_dict={'movies':moviesForm}
    if request.method=='POST':
        moviesForm=MoviesForm(request.POST)
        movies_dict={'movies':moviesForm,'success':success}
        if moviesForm.is_valid():
            moviesForm.save()
            return render(request, 'moviesapp/addMovies.html',movies_dict)
    return render(request, 'moviesapp/addMovies.html',movies_dict)