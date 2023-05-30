from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models

from .constants import (ADMIN, CONF_CODE_MAX_LEN, EMAIL_MAX_LEN,
                        FIRST_NAME_MAX_LEN, LAST_NAME_MAX_LEN, MODERATOR,
                        ROLE_MAX_LEN, USER, USERNAME_MAX_LEN)
from .validators import username_not_me_validator, username_validator


class User(AbstractUser):
    """Модель Пользователя."""

    ROLE_CHOICES = (
        (USER, 'Пользователь'),
        (MODERATOR, 'Модератор'),
        (ADMIN, 'Администратор'),
    )

    username = models.CharField(
        verbose_name='Имя пользователя',
        max_length=USERNAME_MAX_LEN,
        blank=False,
        unique=True,
        help_text='Введите имя пользователя',
        validators=[username_not_me_validator, username_validator],
        error_messages={
            'unique': 'Пользователь с таким именем уже существует',
        },
    )

    email = models.EmailField(
        verbose_name='Адрес электронной почты',
        max_length=EMAIL_MAX_LEN,
        blank=False,
        unique=True,
        help_text='Введите адрес электронной почты',
        error_messages={
            'unique': 'Пользователь с таким email уже существует',
        },
    )

    first_name = models.CharField(
        verbose_name='Имя',
        max_length=FIRST_NAME_MAX_LEN,
        blank=True,
        help_text='Укажите имя',
    )

    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=LAST_NAME_MAX_LEN,
        blank=True,
        help_text='Укажите фамилию',
    )

    bio = models.TextField(
        verbose_name='Биография',
        blank=True,
        help_text='Здесь напишите о себе',
    )

    role = models.CharField(
        verbose_name='Роль пользователя',
        choices=ROLE_CHOICES,
        max_length=ROLE_MAX_LEN,
        default='user',
        help_text='Выберите роль пользователя',
    )

    confirmation_code = models.CharField(
        verbose_name='Код подтверждения',
        blank=True,
        max_length=CONF_CODE_MAX_LEN
    )

    def email_user(
        self,
        message,
        subject='Регистрация',
        from_email='yamdb@yandex.ru',
        **kwargs
    ):
        send_mail(
            subject,
            message,
            from_email,
            [self.email],
            fail_silently=False,
            **kwargs
        )

    @property
    def is_user(self):
        return self.role == USER

    @property
    def is_moderator(self):
        return self.role == MODERATOR

    @property
    def is_admin(self):
        return self.role == ADMIN or self.is_superuser

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('id',)

    def __str__(self):
        return self.username
