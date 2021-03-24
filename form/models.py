from django.db import models

# Create your models here

class Form(models.Model):
    
    first_name = models.CharField(max_length=20,null=True)
    middle_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, null=True)
    phone = models.PositiveIntegerField() 
    gender = models.CharField(max_length=20, choices=(
        ('male','Male'),
        ('Female','Female'),
    ))
    country = models.CharField( max_length=50, choices=(
        ('pakistan','Pakistan'),
        ('uk','Uk'),
    ))

    def __str__(self):
        return self.first_name
    