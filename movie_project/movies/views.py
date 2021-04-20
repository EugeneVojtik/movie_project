from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView

from movies.forms import ReviewForm
from movies.models import Movie, Reviews


class MainPage(ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = 'movie_list.html'


class MovieDetailView(DetailView):
    model = Movie
    slug_field = 'url'


class AddReview(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))
            form.movie_id = pk
            form.save()
        return redirect(f'/{form.movie.url}')


def toMainPage(request):
    return redirect('the-main-page')
