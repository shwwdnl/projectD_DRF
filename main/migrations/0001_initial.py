# Generated by Django 5.0.1 on 2024-01-24 13:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Курс')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='static/preview/', verbose_name='Картинка')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_lesson', models.CharField(max_length=150, verbose_name='Название урока')),
                ('description_lesson', models.TextField(verbose_name='Описание урока')),
                ('preview_lesson', models.ImageField(blank=True, null=True, upload_to='static/lesson/', verbose_name='Картинка')),
                ('url_video', models.URLField(verbose_name='Видео-ссылка')),
                ('course_lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.course', verbose_name='Курс')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
            },
        ),
    ]