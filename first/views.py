from django.shortcuts import render
from django.http import HttpResponse
from .models import Students, Score

# Create your views here.
def index(request):
    return render(request, 'first/index.html')

def students(request):

    #DB에서 데이터 가져와서
    students = Students.objects.all()
    """
        SELECT *
            FROM students
    """
    #템플릿한테 보내주기
    return render(request, 'first/students.html', {
        'text' : '안녕하세요!',
        'students': students
    })

def score(request):
    score = Score.objects.all()
    """
        SELECT * 
            FROM score
    """
    return render(request, 'first/score.html', {
        'score' : score
    })