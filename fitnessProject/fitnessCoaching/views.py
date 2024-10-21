from django.shortcuts import render

# Create your views here.
from .models import Coaches

def display_coaches(request):
    coaches = Coaches.objects.all()
    return render(request,'coaches.html', {'coaches:' coaches})