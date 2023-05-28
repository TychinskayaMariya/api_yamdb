from rest_framework import viewsets 

from .models import Categories, Genres, Title
from rest_framework.permissions import IsAdminUser
from .serializers import (TitleSerializer, CategoriesSerializer,
                          GenresSerializer)
                       
                        
class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = (IsAdminUser,)


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = (IsAdminUser,)


class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
    permission_classes = (IsAdminUser,)
