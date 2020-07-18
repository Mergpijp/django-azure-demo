from django.db import models

# Create your models here.

class Record(models.Model):
    text = models.TextField(max_length=5000, blank=True)