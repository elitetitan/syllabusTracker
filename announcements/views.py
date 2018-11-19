from django.shortcuts import render
from .models import Announcement
# Create your views here.

def announcement_list(request):

    announcements=Announcement.objects.all()

    context={
        'title':'Announcements',
        'announcements':announcements
    }

    return render(request,"announcements/announcement_list.html",context)
