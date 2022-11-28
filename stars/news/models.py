from django.db import models


class News(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название новости')
    intro_text = models.CharField(max_length=200, blank=True, verbose_name='Предисловие')
    content = models.TextField(verbose_name='Контент')
    intro_picture = models.ImageField(upload_to='intro_pictures/%Y/%m/%d', verbose_name='Обложка')
    pictures = models.ManyToManyField('Pictures', blank=True, verbose_name='Изображенния')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    is_published = models.BooleanField(verbose_name='Опубликовано', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class Pictures(models.Model):
    picture = models.ImageField(upload_to='pictures/%Y/%m/%d', verbose_name='Изображение')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering = ['-id']
