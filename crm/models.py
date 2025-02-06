from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class StudentModel(models.Model):

    s_name=models.CharField(max_length=100)
    age=models.PositiveIntegerField()
    course=models.CharField(max_length=100)
    dob=models.DateField()

  
    
