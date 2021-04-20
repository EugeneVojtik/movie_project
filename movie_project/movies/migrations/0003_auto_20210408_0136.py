# Generated by Django 3.2 on 2021-04-07 22:36

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20210408_0102'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.SlugField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=150, verbose_name='Genre')),
                ('description', models.TextField(verbose_name='Genre description')),
            ],
            options={
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genres',
            },
        ),
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.SmallIntegerField(default=0, verbose_name='Value')),
            ],
            options={
                'verbose_name': 'Rating star',
                'verbose_name_plural': 'rating stars',
            },
        ),
        migrations.AlterModelOptions(
            name='movie',
            options={'verbose_name': 'Movie', 'verbose_name_plural': 'Movies'},
        ),
        migrations.RemoveField(
            model_name='movie',
            name='genre',
        ),
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(null=True, related_name='film_actor', to='movies.Actor'),
        ),
        migrations.AddField(
            model_name='movie',
            name='budget',
            field=models.PositiveIntegerField(default=0, help_text='please indicate the amount in dollars', null=True, verbose_name='Budget'),
        ),
        migrations.AddField(
            model_name='movie',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.category'),
        ),
        migrations.AddField(
            model_name='movie',
            name='country',
            field=models.CharField(max_length=100, null=True, verbose_name='Country'),
        ),
        migrations.AddField(
            model_name='movie',
            name='description',
            field=models.TextField(null=True, verbose_name='movie description'),
        ),
        migrations.AddField(
            model_name='movie',
            name='directors',
            field=models.ManyToManyField(null=True, related_name='film_director', to='movies.Actor'),
        ),
        migrations.AddField(
            model_name='movie',
            name='draft',
            field=models.BooleanField(default=False, null=True, verbose_name='Draft'),
        ),
        migrations.AddField(
            model_name='movie',
            name='fees_usa',
            field=models.PositiveIntegerField(default=0, help_text='please indicate the amount in dollars', null=True, verbose_name='USA fees'),
        ),
        migrations.AddField(
            model_name='movie',
            name='fees_world',
            field=models.PositiveIntegerField(default=0, help_text='please indicate the amount in dollars', null=True, verbose_name='world fees'),
        ),
        migrations.AddField(
            model_name='movie',
            name='poster',
            field=models.ImageField(null=True, upload_to='movies/', verbose_name='Poster image'),
        ),
        migrations.AddField(
            model_name='movie',
            name='tagline',
            field=models.CharField(default='', max_length=100, null=True, verbose_name='tag line'),
        ),
        migrations.AddField(
            model_name='movie',
            name='url',
            field=models.SlugField(max_length=160, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='world_premiere',
            field=models.DateField(default=datetime.date.today, null=True, verbose_name='world premiere'),
        ),
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.PositiveSmallIntegerField(default=2021, null=True, verbose_name='Production year'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Movie title'),
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=50, verbose_name='Reviewer name')),
                ('text', models.TextField(max_length=5000, verbose_name='Review')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.reviews', verbose_name='Parent')),
            ],
            options={
                'verbose_name': 'Rating',
                'verbose_name_plural': 'ratings',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15, verbose_name='IP Address')),
                ('movie', models.ForeignKey(on_delete=django.db.models.fields.CharField, to='movies.movie', verbose_name='Movie')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.ratingstar', verbose_name='Star')),
            ],
            options={
                'verbose_name': 'Rating',
                'verbose_name_plural': 'ratings',
            },
        ),
        migrations.CreateModel(
            name='MovieShots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(upload_to='movie_shots/', verbose_name='Image')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
            ],
            options={
                'verbose_name': 'Movie shot',
                'verbose_name_plural': 'Movies shots',
            },
        ),
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(null=True, to='movies.Genre', verbose_name='film_genre'),
        ),
    ]
