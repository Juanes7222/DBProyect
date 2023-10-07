from django.db import models
from django.core.validators import EmailValidator
from django.contrib.auth.models import User
import django

# Create your models here.
class MyUser():
    ...
    
class Forms(models.Model):
    form_id = models.BigAutoField(primary_key=True)
    healthy = models.IntegerField()
    economy = models.IntegerField()
    job = models.IntegerField()
    romance = models.IntegerField()
    personal_growth = models.IntegerField()
    friends = models.IntegerField()
    fun = models.IntegerField()
    self_image = models.IntegerField()
    phy_envio = models.IntegerField()
    date = models.DateField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Psychologist(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    clients = models.ManyToManyField(User)
    

#Nota: un usuario puede tener mas de un formulario hecho, y un formulario esta compuesto por el ponderado de cada seccion
    