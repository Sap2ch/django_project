from django.db import models

class Product(models.Model):
    title = models.CharField(verbose_name='Назва', max_length=100)
    description = models.CharField(verbose_name='Опис товару')
    price = models.FloatField(verbose_name='Ціна')
    currency = models.CharField(verbose_name='Валюта')
    photo = models.ImageField(upload_to='products/')


    def __str__(self):
        """
            ПОВЕРНЕННЯ ПО ТИТУЛЬНІЙ НАЗВІ
        """
        return self.title
