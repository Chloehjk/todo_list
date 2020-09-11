from . import views
from django.urls import path, include

app_name = 'second'

urlpatterns = [
    path('', views.index, name='index'),
    path('favorite_view', views.favorite_view, name='favorite_view'),
    path('favorite_detail/<id>', views.favorite_detail, name='favorite_detail'),
    path('favorite_register', views.favorite_register, name='favorite_register'),
    path('favorite_modify/<id>', views.favorite_modify, name='favorite_modify'),
    path('favorite_delete/<id>', views.favorite_delete, name='favorite_delete'),
    path('todo', views.todo, name='todo'),
    path('todo_detail/<id>', views.todo_detail, name='todo_detail'),
    path('todo_register', views.todo_register, name='todo_register'),
    path('todo_modify/<id>', views.todo_modify, name='todo_modify'),
    path('todo_delete/<id>', views.todo_delete, name='todo_delete'),
]

#path(URL경로 TEXT, views (함수들), 이름!)