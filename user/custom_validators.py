from django.core.exceptions import ValidationError
from django.utils.translation import gettext as gt
from django.contrib.auth.password_validation import CommonPasswordValidator 
import string

class PasswordValidator:
    def __init__(self, password):
        self.password: str = password
        self.min_length = 8
        self.max_length = 16
        
    def validate_min_length(self):
        if len(self.password) < self.min_length:
            raise ValidationError(
                message=gt(f"La constraseña debe de ser de más de {self.min_length} caracteres"),
                code="password_too_short",
                params={
                    "min_length": self.min_length
                })
            
    def validate_max_length(self):
        if len(self.password) > self.max_length:
            raise ValidationError(
                message=gt(f"La contraseña debe de ser menor a {self.max_lenght} caracteres"),
                code="password_too_long",
                params={
                    "max_length": self.max_length})
            
    def validate_mayus_character(self):
        band = False
        for letter in string.ascii_uppercase:
            if letter in self.password:
                band = True
                break
        if not band:
            raise ValidationError(
                message=gt("La contraseña debe de tener mínimo una letra mayúscula"),
                code="password_contain_mayus_char",
                params={"contain_a_mayus": string.ascii_uppercase}
            )
    
    def validate_number(self):
        if not self.password.isalnum():
            raise ValidationError(
                message=gt("La contraseña debe de tener al menos un número"),
                code="password_not_contain_number",
                params={"contain_a_number": string.digit}
            )
            
    def validate_common_password(self):
        validator = CommonPasswordValidator()
        validator(self.password)
            
            


