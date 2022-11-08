# Generated by Django 4.1.2 on 2022-11-08 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0009_actor_movie_actors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='movies', to='movie_app.director'),
        ),
    ]
