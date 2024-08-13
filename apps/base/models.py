# apps/base/models.py
from django.db import models
from ckeditor.fields import RichTextField


class Base(models.Model):
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name='Логотип BIF',
        blank = True, null = True
    )
    logo_2 = models.ImageField(
        upload_to='logo/',
        verbose_name='Логотип GREEN ECONOMY',
        blank = True, null = True
        
    )
    def __str__(self) -> str:
        return "Логотипы"

    class Meta:
        verbose_name = ''
        verbose_name_plural = "Логотипы BIF и GREEN ECONOMY на сайте"
        
        
class Banner(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок для баннера на главной странице"
    )
    descriptions = models.TextField(
        verbose_name="Описание для баннера на главной странице"
    )
    image = models.ImageField(
        upload_to='banners/',
        verbose_name="Фото для баннера на главной странице"
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ""
        verbose_name_plural  = "Настройки баннера на главной странице"
        
class About_the_forum(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок для раздела о форуме"
    )
    descriptions = models.CharField(
        max_length=155,
        verbose_name='Описание для раздела о форуме'
    )
   
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ""
        verbose_name_plural  = "Раздел о форуме на главной странице"
        

class What_will_title(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок для раздела - Что вас будет ждать на главном бизнес событии года"
    )
    descriptions = models.CharField(
        max_length=155,
        verbose_name='Описание для раздела - Что вас будет ждать на главном бизнес событии года'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ""
        verbose_name_plural = "Настройки раздела - Что вас будет ждать на главном бизнес событии года?"

                
class WhatWill(models.Model):
    what_will_title = models.ForeignKey(
        What_will_title,
        related_name="whatwills",
        on_delete=models.CASCADE,
        verbose_name="Заголовок"
    )
    title = models.CharField(
        max_length=155,
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to="image/",
        verbose_name="Фото"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ""
        verbose_name_plural = "Элементы раздела - Что вас будет ждать на главном бизнес событии года?"
        
        
class SliderTitle(models.Model):
    title = models.TextField(
        verbose_name = "Заголовок",
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ""
        verbose_name_plural = "Настройки раздела - Участники выставки"

class Slider(models.Model):
    slidertitle = models.ForeignKey(
        SliderTitle,
        related_name='sliders',
        on_delete=models.CASCADE,
        verbose_name="Заголовок"
    )   
    image = models.ImageField(
        upload_to="image/",
        verbose_name="Фото"
    )

    def __str__(self):
        return str(self.slidertitle)

    class Meta:
        verbose_name = ""
        verbose_name_plural = "Раздел участники выставки на главной странице"

class Video(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок для видео на главной странице"
    )
    descriptions = RichTextField(
        verbose_name='Описание для видео на главной странице'
    ) 
    url = models.URLField(
        verbose_name = "Ссылка на видео",
        null = True, blank = True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ''
        verbose_name_plural = "Настройки видео на главной странице"


class SliderTitleSponsors(models.Model):
    title = models.TextField(
        verbose_name = "Заголовок",
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ""
        verbose_name_plural = "Спонсоры и партнеры - Участники выставки"

class SliderSponsors(models.Model):
    slidertitle = models.ForeignKey(
        SliderTitleSponsors,
        related_name='sliderssponsor',
        on_delete=models.CASCADE,
        verbose_name="Заголовок"
    )   
    image = models.ImageField(
        upload_to="image/",
        verbose_name="Фото"
    )

    def __str__(self):
        return str(self.slidertitle)

    class Meta:
        verbose_name = ""
        verbose_name_plural = "Спонсоры и партнеры на главной странице"

class Button(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = "Кнопка (Подать проект на BIF 2024)"
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ""
        verbose_name_plural = "Подать проект на BIF 2024"