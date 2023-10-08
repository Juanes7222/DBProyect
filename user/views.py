from django.shortcuts import render, redirect
from .models import Forms, Psychologist
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login, get_user_model
from .forms import CreateNewUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .extra_functions import get_questions, get_answers

# Create your views here.

def home(request):
    return render(request, "index.html")

def login_user(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'GET':
        return render(request, 'login.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {"form": AuthenticationForm, "error": "Nombre de usuario o contraseña incorrecto"})

        login(request, user)
        return redirect('dashboard')

@login_required(redirect_field_name="login", login_url="/login/")
def forms(request):
    if request.method == "GET":
        context = {
            "quests": get_questions(),
            "range": range(1, 11, 1)
            }
        return render(request, "form.html", context)
    if not request.POST.get("exit", False):
        get_answers(request.POST, request.user.id)
    return redirect('dashboard')


def register(request):
    data = {
        'form': CreateNewUser()
    }

    if request.method == 'POST':
        user_creation_form = CreateNewUser(data=request.POST)

        if user_creation_form.is_valid():
            user_type = user_creation_form.cleaned_data['user_type']
            
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            if user is not None:
                login(request, user)        
                if user_type == 1:            
                    return redirect('dashboard')
                else:
                    Psychologist.objects.create(
                        user_id=user.id
                    )
                    return redirect("dashboard_psi")
        else:
            data['form'] = user_creation_form

    return render(request, 'register.html', data)

@login_required(redirect_field_name="login", login_url="/login/")
def dashboard(request):
    if request.method == "GET":
        return render(request, "dashboard.html")
    if request.POST.get("exit", False):
        return exit(request)

@login_required
def exit(request):
    if request.method == "GET":
        if request.GET.get("exit") == "not":
            return redirect('dashboard')
    logout(request)
    return redirect('home')

def prueba(request):
    return render(request, "prueba.html")

def forms_views(request):
    return render(request, "forms_views.html")