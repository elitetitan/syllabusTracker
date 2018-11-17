from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Teacher
# Create your views here.

def index(request):

    return render(request,'tracker/layout.html')


def student_list(request):

    students=Student.objects.all()

    context={
        'students':students,
        'title':'Student List'
    }
    return render(request,'tracker/student_list.html',context)

def teacher_list(request):

    teachers=Teacher.objects.all()

    context={
        'teachers':teachers,
        'title':'Instructor List'
    }
    return render(request,'tracker/teacher_list.html',context)