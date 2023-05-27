from django.contrib.auth.tokens import default_token_generator

from ..models import User


def send_confirmation_code(user: User) -> str:
    """Посылает письмо с кодом подтверждения на эл. почту пользователя.
    Возвращает строку с кодом подтверждения.
    """
    confirmation_code = default_token_generator.make_token(user)
    email_message = (
        'Вы получили это письмо, потому что пытались зарегистрироваться \n'
        'или обновить токен на ресурсе YamDB.\n'
        f'Ваше имя пользователя: {user.username}\n'
        'Используйте этот код подтверждения:\n'
        f'"{confirmation_code}"'
    )
    user.email_user(email_message)
    return confirmation_code
