class UserViewSet(ModelViewSet):
    """Вьюсет модели User."""
    pass


class GetAuthTokenApiView(APIView):
    """CBV для получения и обновления токена."""
    pass


@api_view(["POST"])
def signup(request):
    """Добавление нового пользователя."""
    