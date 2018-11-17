from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('students',views.student_list,name='student_list'),
    path('teachers',views.teacher_list,name='teacher_list')
]