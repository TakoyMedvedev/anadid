from django.db import models


class HeroBlock(models.Model):
    background_image = models.ImageField(upload_to='hero_images/', verbose_name='Фоновое изображение')
    title = models.CharField(max_length=255, verbose_name='Заголовок')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Hero блок'
        verbose_name_plural = 'Hero блоки'


class About(models.Model):
    iframe = models.TextField(verbose_name='Видео')
    text = models.TextField(verbose_name='Обо мне')

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'


class Diplom(models.Model):
    image = models.ImageField(upload_to='diplom/', verbose_name='Изображение')

    class Meta:
        verbose_name = 'Diplom'
        verbose_name_plural = 'Diplom'


