from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Forms, Psychologist
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from .forms import CreateNewUser
from django.contrib.auth.forms import AuthenticationForm
from .utils import get_questions, form_manager, get_files_folder, generate_path_img_files, create_zipfile, search_psi, save_integrate
from .decorators import backend_required
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
        if request.user.user_type == 1:
            return redirect('dashboard')
        else:
            return redirect("psi-dashboard")

@login_required(redirect_field_name="login", login_url="/login/")
def forms(request):
    if request.method == "GET":
        context = {
            "quests": get_questions(),
            "range": range(1, 11, 1)
            }
        return render(request, "form.html", context)
    if not request.POST.get("exit", False):
        form_manager(request.POST, request.user.id)
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
                    return redirect("psi-dashboard")
        else:
            data['form'] = user_creation_form

    return render(request, 'register.html', data)

@login_required(redirect_field_name="login", login_url="/login/")
def dashboard(request):
    if request.user.user_type == 2:
        return redirect("psi-dashboard")
    if request.method == "GET":
        form = Forms.objects.filter(user_id=request.user.id)
        context = {
            "id": request.user.id,
            "username": request.user.username,
            "name": request.user.first_name,
            "any_form": form.exists(),
        }
        print(context)
        return render(request, "dashboard.html", context=context)
    if request.POST.get("exit", False):
        return exit(request)

@login_required(redirect_field_name="login", login_url="/login/")
def psi_dashboard(request):
    if request.user.user_type == 1:
        return redirect("dashboard")
    if request.method == "GET":
        return render(request, "dashboard_psi.html")
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

@login_required(redirect_field_name="login", login_url="/login/")
def forms_views(request):        
    #obtiene los datos del front
    date = request.POST.get("date")
    # print(f"{date= }")
    #procesa los datos
    files, dates = get_files_folder(request.user.id, date)
    context = {
        "dates": dates
    }
    selected_files = generate_path_img_files(request.user.id, files)
    context["files"] = selected_files
    
    # print(context)
    
    if request.method == "POST":
        return JsonResponse(context)
    
    context["zip"] = zip(selected_files, dates)
    return render(request, "forms_views.html", context)

def examples(request):
    return render(request, "examples_img.html")

def guide(request):
    return render(request, "guide.html")

@login_required
def view_download_zip(request):
    date = request.GET.get("date", "all")
    # print(request.POST)
    # print(request.GET)
    return create_zipfile(request.user.id, date)

@login_required
def integrations(request):
    context = {
        "post": False
    }
    if request.method == "POST":
        psi = search_psi(request.POST.get("input"))
        if psi:
            context = {
                "name": psi.first_name,
                "last_name": psi.last_name,
                "email": psi.email,
                "since": psi.date_joined.strftime("%A, %d de %B de %Y"),
                "psi_id": psi.id,
                "user_id": request.user.id
            }
        else:
            context = {
                "none": True
            }
    return render(request, "integrations.html", context)

def integrate(request):
    save_integrate(request.POST.get("user_id"), request.POST.get("psi_id"))
    return JsonResponse({"result": True})

#revisar que no se pueda integrar cuando ya se esta integrado
    