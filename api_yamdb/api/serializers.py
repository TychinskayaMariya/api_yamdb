from django.db.models import Avg
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from reviews.models import Categories, Comment, Genres, Review, Title


class CategoriesSerializer(serializers.ModelSerializer):
    """Сериализатор для категории."""
    class Meta:
        model = Categories
        fields = (
            'name',
            'slug',
        )


class GenresSerializer(serializers.ModelSerializer):
    """Сериализатор для жанра."""
    class Meta:
        model = Genres
        fields = (
            'name',
            'slug',
        )


class CreateUpdateTitleSerializer(serializers.ModelSerializer):
    """Сериализатор для произведения."""
    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Categories.objects.all(),
        required=True,
    )

    genre = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Genres.objects.all(),
        many=True,
        required=False,
    )

    class Meta:
        model = Title
        fields = (
            'id',
            'name',
            'year',
            'description',
            'genre',
            'category',
        )


class ShowTitlesSerializer(serializers.ModelSerializer):
    """Сериализатор показа рейтинга для произведений."""
    category = CategoriesSerializer(read_only=True)
    genre = GenresSerializer(many=True, required=False)
    rating = serializers.SerializerMethodField()

    class Meta:
        "Класс дополнен полем 'rating'."
        model = Title
        fields = (
            'id',
            'name',
            'year',
            'rating',
            'description',
            'genre',
            'category',
        )

    def get_rating(self, instance):
        "Метод расчета рейтинга произведения."
        avg = instance.reviews.aggregate(Avg('score'))
        rating = avg['score__avg']
        if rating:
            rating = int(rating)
        else:
            rating = None
        return rating


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализатор для модели ревью."""
    author = SlugRelatedField(slug_field='username', read_only=True,
                              default=serializers.CurrentUserDefault())

    class Meta:
        fields = ('id', 'author', 'text', 'pub_date', 'score')
        model = Review

    def validate(self, data):
        if self.context['request'].method == 'POST':
            reviewer = self.context['request'].user
            title_id = self.context['view'].kwargs['title_id']
            if Review.objects.filter(author=reviewer,
                                     title_id=title_id).exists():
                raise serializers.ValidationError('Повторное ревью запрещено')

        if not 1 <= data['score'] <= 10:
            raise serializers.ValidationError('Оценка от 1 до 10')

        return data


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели комментария."""
    author = SlugRelatedField(slug_field='username', read_only=True,
                              default=serializers.CurrentUserDefault())

    class Meta:
        fields = ('id', 'author', 'text', 'pub_date')
        model = Comment
