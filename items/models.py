from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(default=0,
                                verbose_name='Цена')  # Цена в центах

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    def __str__(self):
        return self.name

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)
