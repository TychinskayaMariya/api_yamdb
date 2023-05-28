from rest_framework import serializers
from .models import Categories, Genres, Title
from rest_framework.relations import SlugRelatedField
from reviews.models import Reviews, Comment


class TitleSerializer(serializers.ModelSerializer):

    """Переопределена категория для возможности записи"""
    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Categories.objects.all(),
        required=True,
    )

    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'category')
        

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
        
        
class ReviewsSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True,
                              default=serializers.CurrentUserDefault())

    class Meta:
        fields = ('id', 'author', 'text', 'pub_date', 'score')
        model = Reviews


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True,
                              default=serializers.CurrentUserDefault())

    class Meta:
        fields = ('id', 'author', 'text', 'pub_date')
        model = Comment
