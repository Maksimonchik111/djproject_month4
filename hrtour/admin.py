from django.contrib import admin
from . import models

admin.site.register(models.Client)
admin.site.register(models.Horse)
admin.site.register(models.HorseTour)
admin.site.register(models.TourComment)
admin.site.register(models.TourCategory)