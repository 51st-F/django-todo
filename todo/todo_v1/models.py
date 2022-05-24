from venv import create
from django.db import models

# Create your models here.
class todo_item(models.Model):
    item = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    finished = models.BooleanField(default=False)
    finished_date = models.DateTimeField(auto_now=True)