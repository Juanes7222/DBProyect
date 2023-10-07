from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateNewUser(UserCreationForm):
 
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'user_type']
  
	def clean_email(self):
		email = self.cleaned_data['email']

		if User.objects.filter(email=email).exists():
			raise forms.ValidationError('Este correo electrónico ya está registrado')
		return email

	def clean_username(self):
		username = self.cleaned_data["username"]
		if User.objects.filter(username=username).exists():
			raise forms.ValidationError("Este usuario ya está en uso")
		return username