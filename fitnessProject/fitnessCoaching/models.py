from django.db import models

class Coaches(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    coaches = [
        ("John Doe", "Strength and Conditioning"),
        ("Jane Smith", "Yoga and Flexibility"),
        ("Michael Brown", "Cardio and Endurance"),
        ("Emily Davis", "Nutrition and Wellness"),
        ("Robert Johnson", "Weightlifting"),
        ("Sarah Williams", "Pilates and Core Training"),
        ("David Miller", "HIIT and Functional Training"),
        ("Linda Taylor", "Dance Fitness"),
        ("James Wilson", "CrossFit Coach"),
        ("Patricia Moore", "Personal Training and Rehab")
    ]

 
    STATUS = [("active", "Active"), ("inactive", "Inactive")]

    body_type = models.CharField(max_length=100, unique=False)  
    coach_age = models.CharField(max_length=2, unique=False)    

    class Meta:
        db_table = "coaches"
