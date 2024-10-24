from django.shortcuts import render, get_object_or_404
from .models import Coaches

def coach_details(request,id):
    coach = get_object_or_404(Coaches, id = id)
    try:
        client = coach.clients
    except Clients.DoesNotExist:
        client = None

    return render(request,'fitnessApp/coaches-clients.html',{
        'coaches': coach,
        'clients' :client if client else "No related client"
    })


def display_coaches(request):
    coach = Coaches.objects.all()
    return render(request,'fitnessApp/all-coaches.html', {'coaches': coach})

