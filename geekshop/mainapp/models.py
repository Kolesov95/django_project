from django.db import models


class ProductCategory(models.Model):
    name = models.CharField('Категория товара', max_length=128)
    description = models.TextField('Описание категории', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Категории продуктов'


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField('имя', max_length=128)
    image = models.ImageField(upload_to='products_images', blank=True)
    description = models.TextField('Описание товара', blank=True)
    short_description = models.CharField('Краткое описание', max_length=256, blank=True)
    price = models.DecimalField('Цена за единицу', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField('Количество товаров', default=0)

    class Meta:
        verbose_name_plural = 'Продукты'
