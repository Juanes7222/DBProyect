from django.db import models
from .models_ignore import AbstractUser
from django.utils import timezone
from .extra_functions import generate_codes
from django.utils.translation import gettext_lazy as _



# Create your models here.

class UserBase(AbstractUser):
    
    user_type = models.IntegerField(verbose_name="Tipo de usuario",
                                    choices=((1, "Usuario normal"), (2, "Psicólogo")),
                                    null=False,
                                    default=1)
    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"
    
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
    user_id = models.ForeignKey(UserBase, on_delete=models.CASCADE)
    
class Psychologist(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=10, default=generate_codes())
    clients = models.ManyToManyField(UserBase)
    

#Nota: un usuario puede tener mas de un formulario hecho, y un formulario esta compuesto por el ponderado de cada seccion
    