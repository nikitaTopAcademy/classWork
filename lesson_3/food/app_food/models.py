from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=20, verbose_name='название продукта')
    price = models.FloatField(verbose_name='цена')
    description = models.TextField(verbose_name='описание')

    class Meta:
        db_table = 'products'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'