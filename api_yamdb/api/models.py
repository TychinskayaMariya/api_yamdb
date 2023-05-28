from django.db import models


class Categories(models.Model):
    name = models.CharField(
        max_length=260,
        unique=True
    )
    slug = models.SlugField(unique=True)
    

class Genres(models.Model):
    name = models.CharField(
        max_length=260,
        unique=True
    )
    slug = models.SlugField(unique=True)


class Title(models.Model):
    """id,name,year,category"""
    category = models.ForeignKey(
        Categories,
        on_delete=models.SET_NULL,
        null=True
    )

    genre = models.ManyToManyField(
        Genres,
        through='TitleGenres',
    )

    name = models.CharField(
        max_length=260,
    )

    year = models.IntegerField()


class TitleGenres(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE)
