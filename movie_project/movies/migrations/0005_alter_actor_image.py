# Generated by Django 3.2 on 2021-04-10 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_alter_rating_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='image',
            field=models.ImageField(blank=True, upload_to='actors/', verbose_name='Image'),
        ),
    ]