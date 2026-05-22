from django.shortcuts import render

def book_view(request):
    if request.method == 'GET':
        context = {
            'title' : "Последнее желание",
            'author' : 'Анджей Сапковский',
            'genre' : 'Dark fantasy'
        }

    return render(request, 'book_list.html', context)
