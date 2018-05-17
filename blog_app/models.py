from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):

    class Meta:
        db_table = 'post'
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['create']

    title = models.CharField('Заголовок', max_length=550)
    text = RichTextUploadingField(blank=True, null=True)
    image = models.ImageField('Изображение', upload_to='post/')
    create = models.DateTimeField('Создано', auto_now=True)

    def __str__(self):
        return self.title
