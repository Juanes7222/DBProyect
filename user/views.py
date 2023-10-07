from django.shortcuts import render, redirect
from .models import Forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login, get_user_model
from .forms import CreateNewUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Create your views here.

def home(request):
    return render(request, "index.html")

def login_user(request):
    if request.method == 'GET':
        return render(request, 'login.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('home')


def forms(request):
    import json
    with open(r"C:\Users\juanb\Documents\Programacion\bdproject\user\questions.json", "r", encoding="utf-8") as file:
        quest = json.load(file)
    context =  {"quests": quest.items(), "range": range(1, 11, 1)}
    print(context["quests"])
    return render(request, "form.html", context)

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
                    return redirect("dashboard_psi")
        else:
            data['form'] = user_creation_form

    return render(request, 'register.html', data)

@login_required
def dashboard(request):
    if request.method == "GET":
        return render(request, "dashboard.html")
    if request.POST.get("exit", False):
        return exit(request)

@login_required
def exit(request):
    logout(request)
    return redirect('home')