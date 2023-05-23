class UserSerializer(serializers.ModelSerializer):
    """Сериализатор модели User."""
    pass


class UserProfileSerializer(UserSerializer):
    """Сериализатор модели User для профиля пользователя."""
    pass


class SignUpSerializer(serializers.Serializer):
    """Сериализатор для регистрации."""
    pass


class GetAuthTokenSerializer(serializers.Serializer):
    """Сериализатор для получения токена."""
    pass
