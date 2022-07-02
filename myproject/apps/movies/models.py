from django.db import models
from django.utils import timezone
import datetime


class Movie(models.Model):
    title = models.CharField('название фильма', max_length=200)
    text = models.TextField('описание')
    pub_date = models.DateTimeField('дата публикации')

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))

    class Meta:
        verbose_name = 'Фильмец'
        verbose_name_plural = 'Фильмецы'


class User(models.Model):
    name = models.CharField('имя', max_length=50)
    surname = models.CharField('имя', max_length=50)
    reg_date = models.DateTimeField('дата регистрации')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'