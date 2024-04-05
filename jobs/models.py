from django.db import models
from django.utils import timezone
from datetime import date
from django.core.validators import RegexValidator

# Create your models here.
class About(models.Model):
    myname = models.CharField(max_length=20, default = "Enter your name in DB")
    dob = models.DateField(default=date.today)
    email = models.EmailField(blank=True, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=True)  # Phone number field allowing blank values
    profile_about = models.CharField(max_length=800, default="Profile Summary")
    city = models.CharField(max_length=200, default = "Saint John, New Brunswick, Canada")
    degree = models.CharField(max_length=100, default = "Masters in Computer Applications")
    roles = models.CharField(max_length=100, default = "Web Developer & Freelancer")
    profileImage = models.ImageField(upload_to='images/', null=True)
    # STATUS_CHOICES = (
    #     ('OTW', 'OpenToWork'),
    #     ('CW', 'CurrentlyWorking'),
    # )
    # status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='OpenToWork')
    # CURRENT_STATUS_CHOICES = (
    #     ('Student', 'Student'),
    #     ('Working', 'Working'),
    #     ('Freelance', 'Freelance'),
    #     ('Looking for Opportunity', 'Looking for Opportunity'),
    # )
    # current_status = models.CharField(max_length=50, choices=CURRENT_STATUS_CHOICES, default='Looking for Opportunity')

    def __str__(self):
        return self.myname 



class Job(models.Model):
    jobImage = models.ImageField(upload_to='images/')
    jobDescription = models.CharField(max_length=200, default="Job Description")
    jobSummary = models.CharField(max_length=800, default="Job Summary")
    #date_of_joining = models.DateField(default=timezone.now, null=True)

    def __str__(self):
        return self.jobDescription
