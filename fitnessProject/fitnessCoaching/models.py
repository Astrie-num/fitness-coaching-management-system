from django.db import models
from clientsApp.models import Clients

class Coaches(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(default = 'example@gmail.com')

    body_type = models.CharField(max_length = 100, unique = False)  
    coach_age = models.IntegerField(unique = False)    

    clients = models.OneToOneField(Clients, on_delete = models.CASCADE, related_name = "coaches", null = True, blank = True)

    class Meta:
        db_table = "coaches"
