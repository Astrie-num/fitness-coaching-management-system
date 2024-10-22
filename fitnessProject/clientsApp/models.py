from django.db import models

class Clients(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()

    STATUS = [("active", "Active"), ("inactive", "Inactive")]

    body_type = models.CharField(max_length=100, unique=False)  
    client_age = models.CharField(max_length=2, unique=False)    

    class Meta:
        db_table = "clients"