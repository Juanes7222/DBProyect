from django.db import models
from django.core.validators import EmailValidator
from django.contrib.auth.models import User
from django.utils import timezone
from .utils import generate_codes
# Create your models here.
    
class Forms(models.Model):
    form_id = models.BigAutoField(primary_key=True)
    salud = models.IntegerField()
    economia = models.IntegerField()
    trabajo = models.IntegerField()
    romance = models.IntegerField()
    crecimiento_personal = models.IntegerField()
    amigos = models.IntegerField()
    diversion = models.IntegerField()
    imagen_propia = models.IntegerField()
    ambiente_fisico = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Psychologist(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=10, default=generate_codes())
    clients = models.ManyToManyField(User, null=True)
    

#Nota: un usuario puede tener mas de un formulario hecho, y un formulario esta compuesto por el ponderado de cada seccion
    