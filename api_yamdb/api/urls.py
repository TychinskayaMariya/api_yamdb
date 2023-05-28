from django.urls import include, path

from rest_framework import routers

from .views import CategoriesViewSet, GenresViewSet, TitleViewSet

router = routers.DefaultRouter()

router.register(r'v1/titles', TitleViewSet, basename='artefact')
router.register(r'v1/categories', CategoriesViewSet)
router.register(r'v1/genres', GenresViewSet)


urlpatterns = [
    path('', include(router.urls), name='api-root'),
]
