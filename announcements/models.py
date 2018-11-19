from django.db import models
from datetime import datetime
# Create your models here.

class Announcement(models.Model):
    announcement=models.TextField()
    published_at=models.DateTimeField(default=datetime.now,blank=True)
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title
    