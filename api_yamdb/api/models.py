from django.db import models


class Title(models.Model):
    category = models.ForeignKey(
        Categories,
        on_delete=models.SET_NULL,
    )

    genre = models.ManyToManyField(
        Genres,
        through='TitleGenres',
    )

    name = models.CharField(
        max_length=48,
    )

    year = models.IntegerField()


class Categories(models.Model):
    name = models.CharField(
        max_length=48,
        unique=True
    )


class Genres(models.Model):
    name = models.CharField(
        max_length=48,
        unique=True
    )


class TitleGenres(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE)