from django.conf import settings
from django.db import models

from users.models import NULLABLE


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=150, verbose_name='Курс')
    preview = models.ImageField(upload_to='static/preview/', verbose_name='Картинка', **NULLABLE)
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    name_lesson = models.CharField(max_length=150, verbose_name='Название урока')
    description_lesson = models.TextField(verbose_name='Описание урока')
    preview_lesson = models.ImageField(upload_to='static/lesson/', verbose_name='Картинка', **NULLABLE)
    url_video = models.URLField(verbose_name='Видео-ссылка')
    course_lesson = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')

    def __str__(self):
        return f'{self.name} - {self.name_lesson} '

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


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