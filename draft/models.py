from django.db import models

# Create your models here.
class Syllabus(models.Model):
    sno=models.IntegerField()
    topic=models.CharField(max_length=100)
    lecture_no=models.CharField(max_length=50)

    def __str__(self):
        return self.topic