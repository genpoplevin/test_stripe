from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=8,
                                decimal_places=2,
                                default=0,
                                verbose_name='Цена')

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    def __str__(self):
        return self.name
