from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    genre_name = models.CharField(max_length=150)

    def __str__(self):
        return self.genre_name


class Movie(models.Model):
    genre = models.ManyToManyField(Genre)
    movie_title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='movies/')
    director = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    budget = models.PositiveIntegerField()
    release_date = models.DateField()
    age_limit = models.PositiveIntegerField()
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.movie_title


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    commentator = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.comment_text} - {self.created_at}'


class VipBooking(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat_number = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.user} - {self.seat_number}'