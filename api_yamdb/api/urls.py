from django.urls import include, path
from rest_framework import routers

from .views import ReviewViewSet, CommentViewSet, CategoriesViewSet, GenresViewSet, TitleViewSet

app_name = 'api'

router = routers.DefaultRouter()

router.register(r'v1/titles', TitleViewSet, basename='artefact')
router.register(r'v1/categories', CategoriesViewSet)
router.register(r'v1/genres', GenresViewSet)
router.register(
    r'titles/(?P<titles_id>\d+)/reviews',
    ReviewViewSet, basename='reviews'
)
router.register(
    r'titles/(?P<titles_id>\d+)/reviews/(?P<reviews_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)


urlpatterns = [
    path('v1/', include(router.urls)),
