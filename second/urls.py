from . import views
from django.urls import path, include

app_name = 'second'

urlpatterns = [
    path('', views.index, name='index'),
    path('favorite_view', views.favorite_view, name='favorite_view'),
    path('favorite_detail/<id>', views.favorite_detail, name='favorite_detail'),
    path('todo', views.todo, name='todo'),
    path('todo_detail/<id>', views.todo_detail, name='todo_detail'),
]

#path(URL경로 TEXT, views (함수들), 이름!)