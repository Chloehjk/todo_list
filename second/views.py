from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Favorite, FavoriteGroup, Todo, TodoGroup
# Create your views here.

def index(request):
    return render(request, 'second/index.html')

def favorite_view(request : HttpRequest):
    data = Favorite.objects.all()
    return render(request, 'second/favorite_view.html', {'favorite': data})

def favorite_detail(request, id):
    data = Favorite.objects.get(pk = id)
    return render(request, 'second/favorite_detail.html', {'detail': data})

def todo(request):
    pending = Todo.objects.filter(status='pending')
    inprogress = Todo.objects.filter(status='inprogress')
    end = Todo.objects.filter(status='end')
    return render(request, 'second/todo.html', {
            'pending': pending,
            'inprogress': inprogress,
            'end': end})


def todo_detail(request, id):
    data = Todo.objects.get(pk = id)
    return render(request, 'second/todo_detail.html', {'detail': data})
    