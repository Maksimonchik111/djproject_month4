from django.http import HttpResponse
from django.shortcuts import render
from . import models
from django.core.paginator import Paginator
from django.db.models import F

def search_view(request):
    query = request.GET.get('s', '')
    if query:
        tours = models.HorseTour.objects.filter(title__icontains=query)
    else:
        return HttpResponse('Блог не найден!')

    return render(request,
                  template_name='tour_list.html',
                  context={'tours': tours})

def tour_list_view(request):
    if request.method == "GET":
        tours = models.HorseTour.objects.all()
        paginator = Paginator(tours, 2)
        page = request.GET.get('page')
        page_obj = paginator.get_page(page)

        return render(request, 'tour_list.html', {'tours': page_obj})

def tour_detail_view(request, id):
    if request.method == 'GET':
        tour = models.HorseTour.objects.get(id=id)

        viewed_blog = request.session.get('viewed_blog', [])

        if id not in viewed_blog:
            tour.views = F("views") + 1
            tour.save()
            tour.refresh_from_db()
            viewed_blog.append(id)
            request.session['viewed_blog'] = viewed_blog

        return render(request, 'tour_detail.html', context={'tour': tour})