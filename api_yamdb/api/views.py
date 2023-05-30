from django.shortcuts import get_object_or_404
from django_filters import rest_framework as myfilters

from rest_framework import filters, viewsets
from rest_framework.pagination import LimitOffsetPagination
# from rest_framework.permissions import IsAdminUser
from reviews.models import Categories, Comment, Genres, Review, Title

from .filters import TitleFilter
from .permissions import IsAuthorOrReadOnly, AdminOrReadOnly
from .serializers import (CategoriesSerializer, CommentSerializer,
                          GenresSerializer, ReviewSerializer,
                          CreateUpdateTitleSerializer, DemoTitlesSerializer)


class ReviewViewSet(viewsets.ModelViewSet):
    """
    Получить список всех отзывов.
    Добавление нового отзыва.
    Получение отзыва по id.
    Обновление отзыва по id.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def get_title(self):
        return get_object_or_404(Title, pk=self.kwargs.get('title_id'))

    def get_queryset(self):
        return self.get_title().reviews.all()

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
    permission_classes = (IsAuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def get_reviews(self):
        return get_object_or_404(Review, pk=self.kwargs.get('reviews_id'))

    def get_queryset(self):
        return self.get_reviews().comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, reviews=self.get_reviews())


class TitleViewSet(viewsets.ModelViewSet):
    """Вьюсет для произведения(ий)."""
    queryset = Title.objects.all()
    serializer_class = CreateUpdateTitleSerializer
    permission_classes = (AdminOrReadOnly,)
    filter_backends = (myfilters.DjangoFilterBackend,)
    filterset_class = TitleFilter

    def get_serializer_class(self):
        """Выбор нужного сериализатора."""
        if self.action in ['list', 'retrieve']:
            return DemoTitlesSerializer
        return CreateUpdateTitleSerializer


class CategoriesViewSet(viewsets.ModelViewSet):
    """Вьюсет для категории."""
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = (AdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class GenresViewSet(viewsets.ModelViewSet):
    """Вьюсет для жанра."""
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
    permission_classes = (AdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'
