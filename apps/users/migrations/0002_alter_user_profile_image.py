# Generated by Django 5.0 on 2023-12-14 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profiles_images/', verbose_name='Фотография пользавтеля'),
        ),
    ]
