from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    profile_image = models.ImageField(
        upload_to='profiles_images/',
        verbose_name='Фотография пользавтеля',
        blank=True,null=True
    )

    def __str(self):
        return self.username
    
    class Meta:
        verbose_name = 'Пользватель'
        verbose_name_plural = 'Пользватели'