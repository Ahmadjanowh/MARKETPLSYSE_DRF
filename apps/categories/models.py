from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название'
    )
    slug = models.SlugField(
        verbose_name='Челевекопятный URL'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создание'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        