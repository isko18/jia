from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class AboutBanner(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок баннера страницы - О проекте"
    )
    descriptions = models.TextField(
        verbose_name="Описание баннера страницы - О проекте"
    )
    image = models.ImageField(
        upload_to='banners/',
        verbose_name="Фото баннера страницы - О проекте"
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ""
        verbose_name_plural  = "Настройки баннера страницы - О проекте"
        
class Statistics(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Сумма (количество)"
    )
    descriptions = models.TextField(
        verbose_name="Описание - суммы (количество)"
    )
      
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ""
        verbose_name_plural  = "Настройки статистики на странице - О проекте"  
        
class About(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок текста"
    )
    descriptions = RichTextField(
        verbose_name="Описание текста"
    )
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = ""
        verbose_name_plural = "Детальное описание о проекте на странице - О проекте"
        
        
class History(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок раздела Истории"
    )
    descriptions = RichTextField(
        verbose_name="Описание раздела Истории"
    )
    year_1 = models.CharField(
        max_length=255,
        verbose_name="Указать 1 год"
    )
    year_2 = models.CharField(
        max_length=255,
        verbose_name="Указать 2 год"
    )
    year_3 = models.CharField(
        max_length=255,
        verbose_name="Указать 3 год"
    )
    year_4 = models.CharField(
        max_length=255,
        verbose_name="Указать 4 год"
    )
    year_5 = models.CharField(
        max_length=255,
        verbose_name="Указать 5 год"
    )
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = ""
        verbose_name_plural = "Перечисление годов на странице - О проекте"
        
        
class HistoryDetail(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок (указать год и заголовок)"
    )
    descriptions = RichTextField(
        verbose_name="Описание (написать описание для этого года)"
    )
    url = models.URLField(
        verbose_name="Ссылка на видео (youtube)",
        blank=True, null=True
    )
    amount_invest = models.CharField(
        max_length=255,
        verbose_name="Объем привлеченных инвестиций (указать цену в $)"
    )
    amount_projet = models.CharField(
        max_length=255,
        verbose_name="Количество заявленных проекто (указать количество)"
    )
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = ""
        verbose_name_plural = "Детальное описание каждого года на странице - О проекте"
        
        
class Gallery(models.Model):
    image = models.ImageField(
        upload_to='image/',
        verbose_name="Фото (нужно добавить фото)"
    )
    
    def __str__(self) -> str:
        return self.image.url if self.image else ""
    
    class Meta:
        verbose_name = ""
        verbose_name_plural = "Галерея на странице - О проекте"
        
class GalleryTitle(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовк (заголовок для раздела фотографии)',
        blank=True, null=True
    )
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = ""
        verbose_name_plural = "Фотографи на странице - О проекте"