from django.db import models

# Create your models here.


class Student(models.Model):
    nom = models.CharField(max_length=255)
    addresse = models.CharField(max_length=255)
    telephone = models.IntegerField()
    email  = models.EmailField(unique=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    classe = models.CharField(max_length=5)
    


    def __str__(self):
        return self.nom
    
