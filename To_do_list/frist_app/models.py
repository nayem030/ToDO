from typing import Any
from django.db import models

# Create your models here.
class ToDoModel(models.Model):
    Tittle=models.CharField(max_length=50)
    Description=models.CharField(max_length=60)
   
    

    
    