from django.db import models

class Clients(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(default = 'example@gmail.com',unique = True)  
    client_age = models.IntegerField(unique = False)    

    class Meta:
        db_table = "clients"