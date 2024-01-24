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

