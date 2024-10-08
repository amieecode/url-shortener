from django.db import models

# Create your models here.
class LinkMapping(models.Model):
    original_url = models.TextField()
    hashing = models.CharField(max_length=10,unique=True)
    creation_date = models.DateTimeField('creation_date')