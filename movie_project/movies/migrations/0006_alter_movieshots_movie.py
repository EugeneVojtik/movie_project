# Generated by Django 3.2 on 2021-04-16 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_alter_actor_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieshots',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_shots', to='movies.movie'),
        ),
    ]
