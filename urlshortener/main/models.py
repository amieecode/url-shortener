from django.db import models

# Create your models here.
class Question(models.Model):
    original_url = models.CharField(max_length=256)
    url_hash = models.CharField(max_length=10)
    creation_date = models.DateTimeField('creation_date')