# Generated by Django 4.0 on 2021-12-12 23:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_alter_movie_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movies', to='movie.category', verbose_name='categoria'),
        ),
    ]
