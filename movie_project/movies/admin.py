from django.contrib import admin

from movies.models import Movie, Actor, Category, Genre, MovieShots, RatingStar, Rating, Reviews


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', "name", 'url')
    list_display_links = ['name']

class ReviewInLine(admin.StackedInline):
    model = Reviews
    extra = 1
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'draft')
    list_display_links = ['title']
    list_filter = ('category', 'year')
    search_fields = ['title', 'category__name']
    inlines = [ReviewInLine]
    save_on_top = True



@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'movie', 'id')
    readonly_fields = ('name', 'email')


admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(MovieShots)
admin.site.register(RatingStar)
admin.site.register(Rating)
