from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Класс пользователя

    :param avatar: Фото пользователя :class:`django.db.models.ImageField`
    """
    avatar = models.ImageField(upload_to='images/', blank=True, null=True)
