from django.db import models

# Create your models here.
class Job(models.Model):
    profile_Image = models.ImageField(upload_to = 'images/')
    #profile
    profile_Summary = models.CharField(max_length = 800)

    def __str__(self):
        return self.profile_Summary
