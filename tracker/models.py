from django.db import models
from draft.models import Syllabus
# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=50)
    roll_no=models.IntegerField()
    group_no=models.CharField(max_length=50)

    def __str__(self):
        return self.name+'-'+self.group_no


class Teacher(models.Model):
    name=models.CharField(max_length=50)
    tid=models.IntegerField()
    group_no=models.CharField(max_length=50)
    isCood=models.BooleanField()
    syllabus=models.ForeignKey(Syllabus,on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return self.name+'-'+self.group_no