from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название")
    author = models.CharField(max_length=150, verbose_name="Автор")
    description = models.TextField(verbose_name="Описание")
    year = models.IntegerField(verbose_name="Год издания")
    pages = models.PositiveIntegerField(verbose_name="Количество страниц")
    genre = models.CharField(max_length=50, verbose_name="Жанр")
    price = models.FloatField(verbose_name="Цена аренды")
    image = models.ImageField(upload_to='books/', verbose_name='Загрузите фото книги')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")
    reservation_days = models.IntegerField(
        validators=[
            MinValueValidator(1, message="Забронировать можно минимум на 1 день"),
            MaxValueValidator(5, message="Забронировать можно максимум на 5 дней")
        ],
        verbose_name="Количество дней бронирования"
    )
    user_comment = models.CharField(max_length=255,blank=True,null=True,verbose_name="Комментарий к бронированию (не обязательно)")

    def __str__(self):
        return f'{self.author} - {self.title}'