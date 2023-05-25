from rest_framework import serializers
from .models import Categories, Genres, Title


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = ('category', 'genre', 'name', 'year')
        

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = (
            'name',
            'slug'
        )


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = (
            'name',
            'slug'
        )