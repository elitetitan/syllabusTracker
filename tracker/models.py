from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=50)
    roll_no=models.IntegerField()
    group_no=models.CharField(max_length=50)


class Teacher(models.Model):
    name=models.CharField(max_length=50)
    tid=models.IntegerField()
    group_no=models.CharField(max_length=50)
    isCood=models.BooleanField()
