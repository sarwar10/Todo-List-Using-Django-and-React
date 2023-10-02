from django.db import models
from django.utils import timezone

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duedate = models.DateField(default= timezone.now)
    completed = models.BooleanField(default=False)


    def __str__(self):
        return self.title
