from django.db import models

# Create your models here.
class Menu(models.Model):
    name=models.CharField(max_length=225)
    image=models.ImageField(upload_to='menu/')
    price=models.DecimalField(max_digits=5,decimal_places=2)


    def __str__(self):
        return self.name
    

class Chef(models.Model):
    name=models.CharField(max_length=225)
    chefimg=models.ImageField(upload_to='chef/')
    email=models.EmailField()

    def __str__(self):
        return self.name
    







