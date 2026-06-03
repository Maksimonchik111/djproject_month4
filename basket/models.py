from django.db import models

class Basket(models.Model):
    product_title = models.CharField(max_length=100)
    product_photo = models.ImageField(upload_to='basket/')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField()
    added_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.product_title


