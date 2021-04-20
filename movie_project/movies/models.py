from datetime import date

from django.db import models
from django.urls import reverse


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = "Categories"

    name = models.CharField("Category", max_length=150)
    url = models.SlugField(max_length=160, unique=True)
    description = models.TextField("Description")

    def __str__(self):
        return self.name


class Actor(models.Model):
    class Meta:
        verbose_name = 'Actors and directors'
        verbose_name_plural = 'Actors and directors'

    name = models.CharField("Actor", max_length=150)
    age = models.PositiveSmallIntegerField("Age", default=0)
    description = models.TextField("description")
    image = models.ImageField('Image', upload_to='actors/', blank=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'

    url = models.SlugField(unique=True, max_length=100)
    name = models.CharField('Genre', max_length=150)
    description = models.TextField("Genre description")

    def __str__(self):
        return self.name


# Create your models here.
class Movie(models.Model):
    title = models.CharField('Movie title', max_length=100)
    tagline = models.CharField('tag line', max_length=100, default='', null=True)
    description = models.TextField('movie description', null=True)
    poster = models.ImageField('Poster image', upload_to='movies/', null=True)
    year = models.PositiveSmallIntegerField('Production year', default=2021, null=True)
    country = models.CharField('Country', max_length=100, null=True)
    directors = models.ManyToManyField(Actor, related_name='film_director', null=True)
    actors = models.ManyToManyField(Actor, related_name='film_actor', null=True)
    genres = models.ManyToManyField(Genre, verbose_name='film_genre', null=True)
    world_premiere = models.DateField("world premiere", default=date.today, null=True)
    budget = models.PositiveIntegerField('Budget', default=0, help_text='please indicate the amount in dollars',
                                         null=True)
    fees_usa = models.PositiveIntegerField("USA fees", default=0, help_text='please indicate the amount in dollars',
                                           null=True)
    fees_world = models.PositiveIntegerField("world fees", default=0, help_text='please indicate the amount in dollars',
                                             null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    url = models.SlugField(unique=True, max_length=160, null=True)
    draft = models.BooleanField('Draft', default=False, null=True)

    def __str__(self):
        return self.title

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = "Movies"

    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={'slug': self.url})


class MovieShots(models.Model):
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE, related_name='movie_shots')
    title = models.CharField('Title', max_length=100)
    description = models.TextField('Description')
    image = models.ImageField('Image', upload_to='movie_shots/')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Movie shot'
        verbose_name_plural = "Movies shots"


class RatingStar(models.Model):
    value = models.SmallIntegerField('Value', default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Rating star'
        verbose_name_plural = "rating stars"


class Rating(models.Model):
    ip = models.CharField('IP Address', max_length=15)
    star = models.ForeignKey("RatingStar", on_delete=models.CASCADE, verbose_name='Star')
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, verbose_name='Movie')

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = "ratings"


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField('Reviewer name', max_length=50)
    text = models.TextField('Review', max_length=5000)
    parent = models.ForeignKey('self', verbose_name='Parent', on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.movie}'

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = "Reviews"
