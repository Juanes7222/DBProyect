from .crud import create_user, create_psi, get_forms, save_integrate, search_psi, get_info_user, save_message_form, get_message_form, get_request, save_requests_integrate, update_request
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from .forms import CreateNewUser
from django.contrib.auth.forms import AuthenticationForm
from .utils import get_questions, form_manager, get_files_folder, generate_path_img_files, create_zipfile, get_users_integrate, get_forms_ids, request_integration
from .decorators import backend_required
# Create your views here.

def home(request):
    return render(request, "global/index.html")

def login_user(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'GET':
        return render(request, 'global/login.html', {"form": AuthenticationForm()})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'global/login.html', {"form": AuthenticationForm(), "error": "Nombre de usuario o contraseña incorrecto"})

        login(request, user)
        if request.user.user_type == 1:
            return redirect('dashboard')
        else:
            return redirect("psi-dashboard")

# @login_required(redirect_field_name="login", login_url="/login/")
def forms(request):
        
    if request.method == "GET":
        context = {
            "quests": get_questions(),
            "range": range(1, 11, 1)
            }
        if request.user.is_anonymous:
            context["anonymous"] = True
        return render(request, "norm_user/form.html", context)
    if not request.POST.get("exit", False):
        if request.POST.get("user", False):
            print(request.POST)
            response = form_manager(request.POST, request.user.id, 2)
            response['Content-Disposition'] = 'attachment; filename="mi_grafico.png"'
            return response
        else:
            form_manager(request.POST, request.user.id, 1)
    return redirect('dashboard')


def register(request):
    data = {
        'form': CreateNewUser()
    }

    if request.method == 'POST':
        user_creation_form = create_user(request)
        if user_creation_form.is_valid():
            user_type = user_creation_form.cleaned_data['user_type']
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            if user is not None:
                login(request, user)        
                if user_type == 1:            
                    return redirect('dashboard')
                else:
                    create_psi(user_id=user.id)
                    return redirect("psi-dashboard")
        else:
            data['form'] = user_creation_form

    return render(request, 'global/register.html', data)

@login_required(redirect_field_name="login", login_url="/login/")
def dashboard(request):
    if request.user.user_type == 2:
        return redirect("psi-dashboard")
    if request.method == "GET":
        form = get_forms(user_id=request.user.id)
        context = {
            "id": request.user.id,
            "username": request.user.username,
            "name": request.user.first_name,
            "any_form": form.exists(),
        }
        # print(context)
        return render(request, "norm_user/dashboard.html", context=context)
    if request.POST.get("exit", False):
        return exit(request)

@login_required(redirect_field_name="login", login_url="/login/")
def psi_dashboard(request):
    if request.user.user_type == 1:
        return redirect("dashboard")
    if request.method == "GET":
        return render(request, "psi_user/dashboard_psi.html", {"name": request.user.first_name.title()})
    if request.POST.get("exit", False):
        return exit(request)

@login_required(redirect_field_name="login", login_url="/login/")
def exit(request):
    if request.method == "GET":
        if request.GET.get("exit") == "not":
            return redirect('dashboard')
    logout(request)
    return redirect('home')

def prueba(request):
    return render(request, "global/prueba.html")

@login_required(redirect_field_name="login", login_url="/login/")
def forms_views(request):        
    info = request.POST.get("download")
    date =  request.POST.get("date")
    if info:
        return create_zipfile(request.user.id, date)
    
    files, dates = get_files_folder(request.user.id, date)
    context = {
        "dates": dates
    }
    selected_files = generate_path_img_files(request.user.id, files)
    context["files"] = selected_files
    forms_ids = get_forms_ids(files)
    context["forms_ids"] = forms_ids
        
    if request.method == "POST":
        return JsonResponse(context)
    context["zip"] = zip(selected_files, dates, forms_ids)
    return render(request, "norm_user/forms_views.html", context)

def examples(request):
    return render(request, "global/examples_img.html")

def guide(request):
    return render(request, "global/guide.html")

@login_required(redirect_field_name="login", login_url="/login/")
def view_download_zip(request):
    date = request.GET.get("date", "all")
    return create_zipfile(request.user.id, date)

@login_required(redirect_field_name="login", login_url="/login/")
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
    return render(request, "norm_user/integrations.html", context)

@login_required(redirect_field_name="login", login_url="/login/")
def integrate(request):
    result = save_integrate(request.POST.get("user_id"), request.POST.get("psi_id"))
    return JsonResponse({"result": result})

@login_required(redirect_field_name="login", login_url="/login/")
def view_info_user(request, client_id):
    if request.method == "POST":
        info = request.POST.get("date")
        date, user_id = tuple(info.split("_"))
        return create_zipfile(user_id, date)
    client = get_info_user(id=int(client_id))
    # print(user_id)
    date = "all"

    files, dates = get_files_folder(client_id, date)
    forms_ids = get_forms_ids(files)
    context = {
        "dates": dates
    }
    selected_files = generate_path_img_files(client_id, files)
    context["files"] = selected_files
        
    context["client"] = f"{client.first_name} {client.last_name}"
    context["client_id"] = client.id
    context["zip"] = zip(selected_files, dates, forms_ids)
    return render(request, "psi_user/view_integrations.html", context)
    
@login_required(redirect_field_name="login", login_url="/login/")
def get_integrates(request):
    if request.user.user_type == 1:
        return redirect("dashboard")
    if request.method == "POST":
        print(request.POST)
        document = request.POST.get("document")
        if document:
            request_integration(document, request.user.id)
            return redirect("psi-dashboard")
        else:
            return redirect("view-integrations", client_id=request.POST.get("integrate"))
    clients = get_users_integrate(request.user.id)
    context ={
        "clients": clients,
    }
    return render(request, "psi_user/integrations.html", context)

@login_required(redirect_field_name="login", login_url="/login/")
def save_message(request):
    message = request.POST.get("message")
    title = request.POST.get("title")
    form_id = request.POST.get("form_id")
    created = save_message_form(message, form_id, title)
    return JsonResponse({"result": created})

def get_message(request, form_id):
    message, title = get_message_form(int(form_id))
    response = {
        "message": message,
        "title": title
    }
    return JsonResponse(response)

def request_integration_manager(request):
    if request.method == "POST":
        req_id = request.POST.get(str(request.user.id))
        psi_id = request.POST.get("psi_id")
        req = get_request(req_id, 2)
        update_request(req)
        save_integrate(request.user.id, int(psi_id))
    reqs = get_request(request.user.id)
    users = [(get_info_user(id=req.user_req_id), req.req_id) for req in reqs if not req.result]
    print(users)
    users = map(lambda x: (x[0].username, x[0].id, x[1]), users)
    context = {
        "users": list(users),
        "userid": request.user.id
    }
    print(context)
    return render(request, "norm_user/request.html", context)
    
    
    