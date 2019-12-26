from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )
    tag = models.ManyToManyField('Tags', through='Relationship', related_name='tags')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Tags(models.Model):
    name = models.CharField(max_length=64, verbose_name='Раздел')

    class Meta:
        ordering = ['name']
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.name


class Relationship(models.Model):
    article = models.ForeignKey(Article, related_name='art_rel', on_delete=models.CASCADE)
    tag = models.ForeignKey(Tags, related_name='tag_rel', on_delete=models.CASCADE)
    is_main = models.BooleanField(verbose_name='Основной', default=False)

    class Meta:
        verbose_name_plural = 'Теги'
