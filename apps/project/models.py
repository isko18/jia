from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Project(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок баннера страницы - Бизнес проекты"
    )
    descriptons = RichTextField(
        verbose_name="Описание баннера страницы - Бизнес проекты"
    )
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = ""
        verbose_name_plural = "Настройки раздела бизнес проекты - Бизнес проекты"
        
class YearlyCatalog(models.Model):
    year = models.IntegerField(
        verbose_name="Год - (Указать год)"
    )
    image = models.FileField(
        upload_to='catalog_pdf/', 
        verbose_name="Изображение - (фото каталога)",
        blank = True, null = True
    )

    def __str__(self):
        return str(self.year)

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Годовые каталоги страницы - Бизнес проекты'
        
class Scroll(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Описание (Нужно написать описание для фото)",
        blank=True, null = True
    )
    image = models.ImageField(
        upload_to='image/',
        verbose_name="фото (Нужно указать изображение)",
        blank=True, null = True
    )
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Перечень необходимого - Бизнес проекты'
        
        
class BusinessProject(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок (Для раздела - Участие открыто для всех предпринимателей с действующим бизнесом!)",
        blank=True, null=True
    )
    descriptons = models.CharField(
        max_length=255,
        verbose_name="Описание (Участие открыто для всех предпринимателей с действующим бизнесом!)",
        blank=True, null=True
    )
    scroll = models.ForeignKey(
        Scroll,
        on_delete=models.CASCADE,
        verbose_name="Перечень необходимого"
    )
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Участие открыто для всех предпринимателей с действующим бизнесом! на странице - Бизнес проекты'
        