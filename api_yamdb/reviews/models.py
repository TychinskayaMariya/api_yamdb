from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from users.models import User


class Categories(models.Model):
    """Модель для категорий."""
    name = models.CharField(
        max_length=260,
        unique=True
    )
    slug = models.SlugField(unique=True)


class Genres(models.Model):
    """Модель для жанров."""
    name = models.CharField(
        max_length=260,
        unique=True
    )
    slug = models.SlugField(unique=True)


class Title(models.Model):
    """Модель для произведений."""
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


class Reviews(models.Model):
    """Модель для отзыва + рейтинг."""
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Отзыв')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор')
    text = models.TextField(verbose_name='Текст отзыва',
                            help_text='Введите текст отзыва')
    pub_date = models.DateTimeField(verbose_name='Дата публикации',
                                    auto_now_add=True)
    score = models.IntegerField(default=0, validators=[MinValueValidator(0),
                                MaxValueValidator(10)])

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-pub_date']


class Comment(models.Model):
    """Модель для комментария к отзыву."""
    reviews = models.ForeignKey(
        Reviews,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Комментарий')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор')
    text = models.TextField(max_length=200, verbose_name='Текст комментария',
                            help_text='Введите текст комментария')
    pub_date = models.DateTimeField(verbose_name='Дата публикации',
                                    auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-pub_date']
