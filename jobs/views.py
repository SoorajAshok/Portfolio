from django.shortcuts import render
from .models import Job, About

# Create your views here.
def homepage(request):
    about = About.objects
    return render(request, 'jobs/index.html', {'abouts':about})