from django.urls import include, path
from rest_framework import routers

from .views import (CategoriesViewSet, CommentViewSet, GenresViewSet,
                    ReviewViewSet, TitleViewSet)

app_name = 'api'

router = routers.DefaultRouter()

router.register(r'categories', CategoriesViewSet, basename='categories')
router.register(r'genres', GenresViewSet, basename='genres')

router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet, basename='reviews'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<reviews_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router.register(r'titles', TitleViewSet, basename='titles')

urlpatterns = [
    path('v1/', include(router.urls)),
]
