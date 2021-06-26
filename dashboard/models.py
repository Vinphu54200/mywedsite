from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tittle = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.tittle

    class Meta:
        verbose_name="notes"
        verbose_name_plural="notes"

class Homework(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    tittle =models.CharField(max_length=100)
    descirption = models.TextField()
    due = models.DateTimeField()
    is_finished = models.BooleanField(default=False)


    def __str__(self):
        return self.tittle

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tittle = models.CharField(max_length=100)
    is_finished = models.BooleanField(default=False)