from .import views
from django.urls import path, include

app_name='first'

urlpatterns = [
    path('', views.index, name='index'),
    path('students/', views.students, name='students'),
    path('score/', views.score, name='score'), 
    path('students/add', views.student_add, name='student_add'),
    path('students/modify<int:id>', views.student_modify, name='student_modify'),
]

#path(URL경로 TEXT, views (함수들), 이름!)