from django.urls import path

from movies.views import MainPage, MovieDetailView, AddReview, toMainPage

urlpatterns = [
    path('', MainPage.as_view(), name='movie_list'),
    path('<str:slug>/', MovieDetailView.as_view(), name='movie_detail'),
    path("add_review/<int:pk>/", AddReview.as_view(), name='add_review'),
    path('ToMainPage', toMainPage, name='ToMainPage'),
]