from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Students, Score
from .forms import StudentForm, StudentModelForm

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
    if request.method == 'GET':
        return render(request, 'first/score.html', {
            'score' : score
        })
    elif request.method == 'POST':
        Score.objects.create(
            name=request.POST['name'],
            math=request.POST['math'],
            english=request.POST['english'],
            science=request.POST['science'],
        )
        return redirect('first:score')



def student_add(request):
    if request.method == 'GET':
        # form = StudentForm()
        form = StudentModelForm()
        return render(request, 'first/student_add.html',
            {'form':form
            })
    elif request.method == 'POST':
        form = StudentModelForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save()
            return redirect("first:students")
        else:
            return render(request, 'first/student_add.html',{
            'form': form
            })

        #이건 일반 폼
        # form = StudentForm(request.POST)

        # if form.is_valid():

        #     #잘입력됐을경우
        #     Students.objects.create(
        #     name=form.cleaned_data['name'],
        #     address=form.cleaned_data['address'],
        #     email=form.cleaned_data['email']
        # )
        #     return redirect('first:students')

        # else:
        #     return render(request, 'first/student_add.html',{
        #         'form': form
        #     })

        # Students.objects.create(
        #     name=request.POST['name'],
        #     address=request.POST['address'],
        #     email=request.POST['email']
        # )

        # return redirect('first:students')
        # students = Students.objects.all()
        # return render(request, 'first/student_add.html', {
        #         'students':students
        # })

def student_modify(request, id):
    try:
        student = Students.objects.get(pk=id)
    except:
        raise Http404('404')
    if request.method == 'GET':
        form = StudentModelForm(instance=student)
        return render(request, 'first/student_modify.html', {
            'form':form
        })
    elif request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("first:students")
        else:
            return render(request, 'first/student_add.html', {
                'form':form
            })
