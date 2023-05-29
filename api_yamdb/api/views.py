from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAdminUser
from reviews.models import Categories, Comment, Genres, Reviews, Title

from .permissions import IsAuthorOrReadOnly
from .serializers import (CategoriesSerializer, CommentSerializer,
                          GenresSerializer, ReviewsSerializer, TitleSerializer)


class ReviewViewSet(viewsets.ModelViewSet):
    """
    Получить список всех отзывов.
    Добавление нового отзыва.
    Получение отзыва по id.
    Обновление отзыва по id.
    """
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    permission_classes = (IsAuthorOrReadOnly, IsAdminUser,)
    pagination_class = LimitOffsetPagination

    def get_title(self):
        return get_object_or_404(Title, pk=self.kwargs.get('title_id'))

    def get_queryset(self):
        return self.get_title().reviews

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, title=self.get_title())


class CommentViewSet(viewsets.ModelViewSet):
    """
    Получить список всех комментариев.
    Добавление нового комментария к отзыву.
    Получить комментарий по id.
    Обновление комментария по id.
    Удаление комментария.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly, IsAdminUser,)
    pagination_class = LimitOffsetPagination

    def get_reviews(self):
        return get_object_or_404(Reviews, pk=self.kwargs.get('reviews_id'))

    def get_queryset(self):
        return self.get_reviews().comments

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_reviews())


class TitleViewSet(viewsets.ModelViewSet):
    """Вьюсет для произведения."""
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = (IsAdminUser,)


class CategoriesViewSet(viewsets.ModelViewSet):
    """Вьюсет для категории."""
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = (IsAdminUser,)


class GenresViewSet(viewsets.ModelViewSet):
    """Вьюсет для жанра."""
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
    permission_classes = (IsAdminUser,)
