# Generated by Django 5.1.5 on 2025-02-03 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iframe', models.TextField(verbose_name='Видео')),
                ('text', models.TextField(verbose_name='Обо мне')),
            ],
            options={
                'verbose_name': 'About',
                'verbose_name_plural': 'About',
            },
        ),
    ]
