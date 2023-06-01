from django.shortcuts import get_object_or_404
from django_filters import rest_framework as myfilters
from rest_framework import filters, viewsets
from rest_framework.pagination import LimitOffsetPagination
from reviews.models import Categories, Comment, Genres, Review, Title

from .filters import TitleFilter
from .mixins import GetListCreateDeleteMixin
from .permissions import IsAdminOrReadOnly, IsAuthorOrReadOnly
from .serializers import (CategoriesSerializer, CommentSerializer,
                          CreateUpdateTitleSerializer, ShowTitlesSerializer,
                          GenresSerializer, ReviewSerializer)


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
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (myfilters.DjangoFilterBackend,)
    filterset_class = TitleFilter

    def get_serializer_class(self):
        """
        Выбор нужного сериализатора:
        - создать произведение, обновить;
        - показать рейтинг произведения.
        """
        if self.action in ['list', 'retrieve']:
            return ShowTitlesSerializer
        return CreateUpdateTitleSerializer


class CategoriesViewSet(GetListCreateDeleteMixin):
    """Вьюсет для категории."""
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class GenresViewSet(GetListCreateDeleteMixin):
    """Вьюсет для жанра."""
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'
