from django.db import models
from ckeditor.fields import RichTextField

class Exhibition(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок баннера страницы - Выставка"
    )
    descriptions = RichTextField(
        verbose_name="Описание баннера страницы - Выставка"
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


