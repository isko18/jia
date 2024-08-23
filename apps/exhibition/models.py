from django.db import models
from ckeditor.fields import RichTextField

class Exhibition(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок страницы - Выставка"
    )
    descriptions = RichTextField(
        verbose_name="Описание страницы - Выставка"
    )
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = ""
        verbose_name_plural = "Настройки баннера страницы - Выставка"
        
        
class Slider(models.Model):
    image = models.ImageField(
        upload_to='slider_exhibition',
        verbose_name="Фото (первое фото, будет сверху)"
    )
    image_2 = models.ImageField(
        upload_to='slider_exhibition',
        verbose_name="Фото (второе фото, будет снизу)"
    )
    def __str__(self) -> str:
        return self.image.url if self.image else ""
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Настройки слайдера на странице - Выставка'
        
class RentStand(models.Model):
    url_ru = models.URLField(
        verbose_name = 'Арендовать стенд (ссылка на рус.)'
    )
    url_ky = models.URLField(
        verbose_name = "Арендовать стенд (ссылка на кырг.)"
    )
    
    def __str__(self):
        return self.url_ru
    
    class Meta:
        verbose_name = ""
        verbose_name_plural = "Арендовать стенд"


