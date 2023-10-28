from django.db import models
from .models_ignore import AbstractUser
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserBase(AbstractUser, models.Model):
    
    user_type = models.IntegerField(verbose_name="Tipo de usuario",
                                    choices=((1, "Usuario normal"), (2, "Psicólogo")),
                                    null=False,
                                    default=1)
    
    document = models.CharField(max_length=20, blank=False, unique=True, verbose_name="N° de Documento")
    
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
    message = models.TextField(max_length=200, null=True)
    message_title = models.TextField(max_length=30, null=True)
    img = models.ImageField(upload_to="wheels/", null=True)
    img_name = models.CharField(max_length=20, null=True)
    
class Psychologist(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=10, default=get_random_string(length=12), unique=True)
    clients = models.ManyToManyField(UserBase)
    
class Requests(models.Model):
    req_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(UserBase, on_delete=models.CASCADE)
    result = models.BooleanField(default=False)
    user_req = models.ForeignKey(Psychologist, on_delete=models.CASCADE)
    

#Nota: un usuario puede tener mas de un formulario hecho, y un formulario esta compuesto por el ponderado de cada seccion
    