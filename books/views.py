from django.http import HttpResponse
from django.shortcuts import render
from . import models
from django.core.paginator import Paginator
from django.db.models import F


def search_view(request):
    query = request.GET.get('s', '')
    if query:
        books = models.Book.objects.filter(title__icontains=query)
    else:
        return HttpResponse('Блог не найден!')

    return render(request,
                  template_name='book_list.html',
                  context={'books': books})

def book_list_view(request):
    if request.method == 'GET':
        books = models.Book.objects.all().order_by('-id')
        paginator = Paginator(books, 3)
        page = request.GET.get('page')
        page_obj = paginator.get_page(page)

        return render(request,'book_list.html',context={'books': page_obj})



def book_detail_view(request, id):
    if request.method == 'GET':
        book = models.Book.objects.get(id=id)

        viewed_blog = request.session.get('viewed_blog', [])

        if id not in viewed_blog:
            book.views = F("views") + 1
            book.save()
            book.refresh_from_db()
            viewed_blog.append(id)
            request.session['viewed_blog'] = viewed_blog

        return render(request, 'book_detail.html', context={'book': book})
