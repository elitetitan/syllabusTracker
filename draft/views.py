from django.shortcuts import render
from .models import Syllabus
from .forms import SyllabusForm
from django.shortcuts import redirect
# Create your views here.

def syllabus_view(request):

    syllabus=Syllabus.objects.all()

    context={
        'syllabus':syllabus,
        'title':'Course Syllabus'
    }

    return render(request,'draft/syllabus_view.html',context)


def syllabus_draft(request):
    if request.method == 'POST':

        form=SyllabusForm(request.POST)
        if form.is_valid():
            entry=form.save()
            entry.save()
            return redirect('syllabus_view')
    else:
        form=SyllabusForm()


    context={
        'form':form
    }
    return render(request,'draft/syllabus_draft.html',context)