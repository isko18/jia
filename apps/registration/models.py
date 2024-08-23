from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Registration(models.Model):
    title = models.CharField(
        max_length=255, 
        verbose_name="Заголовок банера (на странице Регистрация на форум)"
    )
    descriptions = models.TextField(
        verbose_name = "Описание банера (на странице Регистрация на форум)"
    )
    
    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = ""
        verbose_name_plural = 'Настройки банера страницы -  Регистрация на форум'
        
        
class Standart(models.Model):
    title = models.CharField(
        max_length = 255, 
        verbose_name = "Заголовок билета 'Стандарт'"
    )
    descriptions = RichTextField(
        verbose_name="Описание билета 'Стандарт'"
    )
    
    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = ""
        verbose_name_plural = "Настройки билета Стандарт на странице -  Регистрация на форум"
        
        
class Vip(models.Model):
    title = models.CharField(
        max_length = 255, 
        verbose_name = "Заголовок билета 'VIP'"
    )
    descriptions = RichTextField(
        verbose_name="Описание билета 'VIP'"
    )
    
    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = ""
        verbose_name_plural = 'Настройки билета VIP на странице -  Регистрация на форум'
        
class SectorStandart(models.Model):
    name = models.CharField(max_length=255, verbose_name="Выбрать (добавить новый сектор)")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Добавление секторов для Стандартного пакета на странице - Регистрация на форум'

class ReachStandart(models.Model):
    full_name = models.CharField(
        max_length=255,
        verbose_name="ФИО"
    )
    name_company = models.CharField(
        max_length=255,
        verbose_name='Название вашей компании'
    )
    sector = models.ForeignKey(
        SectorStandart,
        on_delete=models.CASCADE,
        verbose_name="Укажите сектор (Нужно создать или добавить)"
    )
    current = models.CharField(
        max_length=255,
        verbose_name='Количество билетов'
    )
    email = models.CharField(
        max_length=255,
        verbose_name="Электронная почта"
    )
    phone = models.CharField(
        max_length=255,
        verbose_name="Номер телефона"
    )

    def __str__(self) -> str:
        return self.full_name

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Форма бронирования для Стандартного пакета - Регистрация на форум'
         
         
class SectorVip(models.Model):
    name = models.CharField(max_length=255, verbose_name="Выбрать (добавить новый сектор)")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Добавление секторов для VIP пакета на странице - Регистрация на форум'

class ReachVip(models.Model):
    full_name = models.CharField(
        max_length=255,
        verbose_name="ФИО"
    )
    name_company = models.CharField(
        max_length=255,
        verbose_name='Название вашей компании'
    )
    sector = models.ForeignKey(
        SectorVip,
        on_delete=models.CASCADE,
        verbose_name="Укажите сектор (Нужно создать или добавить)"
    )
    current = models.CharField(
        max_length=255,
        verbose_name='Количество билетов'
    )
    email = models.CharField(
        max_length=255,
        verbose_name="Электронная почта"
    )
    phone = models.CharField(
        max_length=255,
        verbose_name="Номер телефона"
    )

    def __str__(self) -> str:
        return self.full_name

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Форма бронирования для VIP пакета - Регистрация на форум'
         