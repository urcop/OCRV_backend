from uuid import uuid4

from ckeditor.fields import RichTextField
from django.db import models


class News(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    title = models.CharField(max_length=255, verbose_name='Название')
    description = RichTextField(verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title
