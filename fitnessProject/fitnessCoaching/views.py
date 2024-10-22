from django.shortcuts import render
from .models import Coaches

def display_coaches(request):
    coaches = Coaches.objects.all()
    return render(request,'fitnessApp/coaches.html', {'coaches': coaches})