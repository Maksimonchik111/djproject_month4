from django.shortcuts import render
from . import models


def book_list_view(request):
    if request.method == 'GET':
        books = models.Book.objects.all()

        return render(request,'book_list.html',context={'books': books})


def book_detail_view(request, id):
    if request.method == 'GET':
        book = models.Book.objects.get(id=id)

        return render(request, 'book_detail.html', context={'book': book})