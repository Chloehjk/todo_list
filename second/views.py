from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, Http404
from .models import Favorite, FavoriteGroup, Todo, TodoGroup
from .forms import FavoriteModelForm, TodoModelForm
# Create your views here.

def index(request):
    return render(request, 'second/index.html')

def favorite_view(request : HttpRequest):
    data = Favorite.objects.all()
    return render(request, 'second/favorite_view.html', {'favorite': data})

def favorite_detail(request, id):
    data = Favorite.objects.get(pk = id)
    return render(request, 'second/favorite_detail.html', {'detail': data})


def favorite_register(request : HttpRequest):
    if request.method == 'GET':
        form = FavoriteModelForm()
        return render(request, 'second/favorite_register.html', {
            'form':form
        })

    elif request.method == 'POST':
        form = FavoriteModelForm(request.POST, request.FILES)    
        if form.is_valid():
            post = form.save()
            return redirect('second:favorite_view')
        else:
            return render(request, 'second/favorite_register.html',{'form':form})


def favorite_modify(request : HttpRequest, id):
    try:
        favorite = Favorite.objects.get(pk=id)
    except:
        raise Http404('404')
    if request.method == 'GET':
        form = FavoriteModelForm(instance=favorite)
        return render(request, 'second/favorite_modify.html', {
            'form':form
        })

    elif request.method == 'POST':
        form = FavoriteModelForm(request.POST, instance=favorite)    
        if form.is_valid():
            post = form.save()
            return redirect('second:favorite_view')
        else:
            return render(request, 'second/favorite_modify.html',{'form':form})

def favorite_delete(request, id):
    favorite = Favorite.objects.get(pk=id)
    favorite.delete()
    return redirect('second:favorite_view')


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
    
def todo_register(request : HttpRequest):
    if request.method == 'GET':
        form = TodoModelForm()
        return render(request, 'second/todo_register.html', {
            'form':form
        })

    elif request.method == 'POST':
        form = TodoModelForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('second:todo')
        else:
            return render(request, 'second/todo_register.html',{'form':form})


def todo_modify(request : HttpRequest, id):
    try:
        todo = Todo.objects.get(pk=id)
    except:
        raise Http404('404')
    if request.method == 'GET':
        form = TodoModelForm(instance=todo)
        return render(request, 'second/todo_modify.html', {
            'form':form
        })

    elif request.method == 'POST':
        form = TodoModelForm(request.POST, instance=todo)    
        if form.is_valid():
            post = form.save()
            return redirect('second:todo')
        else:
            return render(request, 'second/todo_modify.html',{'form':form})

def todo_delete(request, id):
    todo = Todo.objects.get(pk=id)
    todo.delete()
    return redirect('second:todo')