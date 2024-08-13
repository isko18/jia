# Generated by Django 4.2.3 on 2024-08-06 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': '', 'verbose_name_plural': 'Настройки раздела бизнес проекты - Бизнес проекты'},
        ),
        migrations.AlterField(
            model_name='yearlycatalog',
            name='image',
            field=models.FileField(upload_to='catalog_pdf/', verbose_name='Изображение - (фото каталога)'),
        ),
        migrations.AlterField(
            model_name='yearlycatalog',
            name='image_en',
            field=models.FileField(null=True, upload_to='catalog_pdf/', verbose_name='Изображение - (фото каталога)'),
        ),
        migrations.AlterField(
            model_name='yearlycatalog',
            name='image_ky',
            field=models.FileField(null=True, upload_to='catalog_pdf/', verbose_name='Изображение - (фото каталога)'),
        ),
        migrations.AlterField(
            model_name='yearlycatalog',
            name='image_ru',
            field=models.FileField(null=True, upload_to='catalog_pdf/', verbose_name='Изображение - (фото каталога)'),
        ),
    ]
