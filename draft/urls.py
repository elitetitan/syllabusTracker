from django.urls import path
from . import views

urlpatterns=[
    path('',views.syllabus_view,name='syllabus_view'),
    path('draft/',views.syllabus_draft,name='syllabus_draft')
]