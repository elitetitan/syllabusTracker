from django.db import models

# Create your models here.
class Syllabus(models.Model):
    sno=models.IntegerField()
    topic=models.TextField()
    lecture_no=models.CharField(max_length=50)
    class Meta:
        verbose_name_plural="Syllabus"
    def __str__(self):
        return self.topic