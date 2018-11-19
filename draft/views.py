from django.shortcuts import render
from .models import Syllabus
# Create your views here.

def syllabus_view(request):

    syllabus=Syllabus.objects.all()

    context={
        'syllabus':syllabus,
        'title':'Course Syllabus'
    }

    return render(request,'draft/syllabus_view.html',context)