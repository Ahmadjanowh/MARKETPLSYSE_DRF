# Generated by Django 5.0 on 2023-12-13 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(max_length=500, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='post_images/', verbose_name='Фотография')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
            },
        ),
    ]
