from django.db import models

class Post(models.Model):

    class Meta:
        db_table = 'post'
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['create']

    title = models.CharField('Заголовок', max_length=140)
    text = models.TextField('Текст статьи')
    image = models.ImageField('Изображение', upload_to='post/')
    create = models.DateTimeField('Создано', auto_now=True)

    def __str__(self):
        return self.title
