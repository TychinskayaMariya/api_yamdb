from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAdminUser

from reviews.models import Reviews, Comment
from .serializers import ReviewsSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly


class ReviewViewSet(viewsets.ModelViewSet):
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
