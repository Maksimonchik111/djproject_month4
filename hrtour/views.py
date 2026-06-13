from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from . import models
from django.core.paginator import Paginator
from django.db.models import F
from django.views import generic


class SearchView(generic.ListView):
    template_name = 'tour_list.html'
    context_object_name = 'tours'
    model = models.HorseTour

    def get_queryset(self):
        return self.model.objects.filter(title__icontains=self.request.GET.get('s'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = self.request.GET.get('s')
        return context

class TourListView(generic.ListView):
    template_name = 'tour_list.html'
    model = models.HorseTour
    context_object_name = 'tours'
    paginate_by = 2

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['tour'] = context['page_obj']
        return context


class TourDetailView(generic.DetailView):
    template_name = 'tour_detail.html'
    context_object_name = 'tour_id'
    pk_url_kwarg = 'id'
    model = models.HorseTour

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        request = self.request
        views_blog = request.session.get('viewed_blog', [])

        if obj.pk not in views_blog:
            self.model.objects.filter(pk=obj.pk).update(views=F('views') + 1)
            views_blog.append(obj.pk)
            request.session['viewed_blog'] = views_blog
            obj.refresh_from_db()
        return obj