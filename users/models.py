from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {
    'null': True,
    'blank': True
}
# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    phone = models.CharField(max_length=40, verbose_name='Номер телефона', **NULLABLE)
    city = models.CharField(max_length=40, verbose_name='Город', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'