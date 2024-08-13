from django.db import models
from ckeditor.fields import RichTextField

class Sector(models.Model):
    name = models.CharField(max_length=255, verbose_name="Выбрать (добавить новый сектор)")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Добавление секторов на странице - Источники финансирования'
        verbose_name_plural = 'Секторы'



class LegalName(models.Model):
    name = models.CharField(max_length=255, verbose_name="Выбрать (добавить юридическое название)")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Добавление юридических названий на странице - Источники финансирования'


class Financing(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок баннера страницы - Источники финансирования"
    )
    image = models.ImageField(
        upload_to='image/',
        max_length=255,
        verbose_name = "Фото баннера страницы - Источники финансирования"
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Настройки баннера страницы - Источники финансирования'
        
class Image(models.Model):
    image = models.ImageField(
        upload_to = 'image/',
        verbose_name = "Фото"
    )
    
    def __str__(self) -> str:
        return self.image.url if self.image else ""
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Настройки фото - Источники финансирования'
        
class Reach(models.Model):
    full_name = models.CharField(
        max_length=255,
        verbose_name="ФИО"
    )
    name_company = models.CharField(
        max_length=255,
        verbose_name='Название вашей компании'
    )
    legal_name = models.ForeignKey(
        LegalName,
        on_delete=models.CASCADE,
        verbose_name="Юридическое название (Нужно создать или добавить)"
    )
    brief_description = models.CharField(
        max_length=255,
        verbose_name="Краткое описание деятельности вашей компании"
    )
    sector = models.ForeignKey(
        Sector,
        on_delete=models.CASCADE,
        verbose_name="Укажите сектор (Нужно создать или добавить)"
    )

    def __str__(self) -> str:
        return self.full_name

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Форма связи на странице - Источники финансирования'
        
class ImageForm(models.Model):
    image = models.ImageField(
        upload_to='image/',
        verbose_name="Фото"
    )

    def __str__(self) -> str:
        return self.image.url if self.image else ""
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Информация фото на странице - Источники финансирования'

class NameInfo(models.Model):
    image_form = models.ForeignKey(
        ImageForm,
        related_name='name_infos',
        on_delete=models.CASCADE,
        verbose_name="Добавить Заголовок и Описание"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    descriptions = models.TextField(
        verbose_name="Описание"
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Информация на странице - Источники финансирования'