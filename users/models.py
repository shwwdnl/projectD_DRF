from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

from main.models import Course, Lesson

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


class Payments(models.Model):
    CASH_PAY = 'Оплата наличными'
    NON_CASH_PAY = 'Оплата по безналу'

    WAYS_PAY = (
        (CASH_PAY, 'Налиными'),
        (NON_CASH_PAY, 'Безналом')
    )

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='Пользователь', **NULLABLE)
    date_pay = models.TimeField(auto_now_add=True, verbose_name='Время платежа')
    course_pay = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Оплаченный курс', **NULLABLE)
    lesson_pay = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Оплаченный урок', **NULLABLE)
    sum_pay = models.IntegerField(verbose_name='Сумма оплаты')
    way_pay = models.CharField(choices=WAYS_PAY, verbose_name='Вариант оплаты')

    def __str__(self):
        return (f'Платеж {self.owner} за курс {self.course_pay}, '
                f'за урок {self.lesson_pay} на сумму {self.sum_pay}')

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'