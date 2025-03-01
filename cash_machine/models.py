from django.db import models

NULLABLE = {"blank": True, "null": True}


class Item(models.Model):
    """Модель товара"""

    title = models.CharField(max_length=255, verbose_name="Наименование товара")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Стоимость товара"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
