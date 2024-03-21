from django.db import models

# Create your models here.
class Jobs(models.Model):
    profile_Image = models.ImageField(upload_to = 'images/')
    profile_Summary = models.CharField(max_length = 200)
