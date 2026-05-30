from django.db import models

class Client(models.Model):
    full_name = models.CharField(max_length=100)
    personal_number = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return f'{self.full_name} - {self.personal_number}'

class Horse(models.Model):
    name = models.CharField(max_length=150)
    booked_by = models.OneToOneField(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class TourCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class HorseTour(models.Model):
    title = models.CharField(max_length=75)
    description = models.TextField()
    category = models.ManyToManyField(TourCategory)

    def __str__(self):
        return self.title


class TourComment(models.Model):
    tour = models.ForeignKey(HorseTour, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.text
