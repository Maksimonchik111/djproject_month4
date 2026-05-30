from django.shortcuts import render
from . import models

def tour_list_view(request):
    if request.method == "GET":
        tours = models.HorseTour.objects.all()

        return render(request, 'tour_list.html', {'tours': tours})
