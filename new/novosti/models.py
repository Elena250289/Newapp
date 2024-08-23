from django.db import models


class Artiles(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    anons = models.CharField('Коротко', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateField('Дата публикации')

    # Без __str__ будет выводиться некрасивая запись
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
