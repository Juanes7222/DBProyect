from .models import UserBase, Psychologist, Forms, Requests
from .forms import CreateNewUser


def get_info_user(**kwargs):
    user = UserBase.objects.get(**kwargs)
    # query = f"SELECT * FROM user_psychologist_clients WHERE userbase_id={user_id}"
    # integrations = Psychologist.clients.raw(query)
    # data = {
    #     "user": user,
    #     "integrations": integrations
    # }
    return user

def get_info_psi(**kwargs):
    user = Psychologist.objects.get(**kwargs)
    return user

def save_requests_integrate(**kwargs):
    req = Requests.objects.create(**kwargs)
    
def get_request(arg, __case=1):
    if __case == 1:
        req = Requests.objects.filter(user_id=arg)
    else:
        req = Requests.objects.get(req_id=arg)
        
    return req
    
def update_request(request):
    request.result = True
    request.save()

def save_message_form(message, form_id, message_title):
    form = Forms.objects.get(form_id=form_id)
    form.message = message
    form.message_title = message_title
    form.save()
    return True
    
def get_message_form(form_id):
    form = Forms.objects.get(form_id=form_id)
    message = form.message
    title = form.message_title
    return message, title

def save_answers(answers):
    form = Forms.objects.create(
        **answers
    )
    return form

def save_integrate(user_id, psi_id):
    psi = Psychologist.objects.get(user_id=psi_id)
    user = UserBase.objects.get(id=user_id)
    try:
        if psi.clients.get(id=user_id):
            return False
        psi.clients.add(user)
    except UserBase.DoesNotExist:
        psi.clients.add(user)
    return True

def create_user(data):
    user_creation_form = CreateNewUser(data=data.POST)

    if user_creation_form.is_valid():
        user_creation_form.save()
    return user_creation_form
    
        
def create_psi(**kwargs):
    Psychologist.objects.create(**kwargs)
    
def get_forms(**kwargs):
    form = Forms.objects.filter(**kwargs)
    return form

def search_psi(userinput):
    # qwery = f"SELECT first_name, last_name, date_joined, email, id FROM user_userbase WHERE username='{userinput}'"
    user_filter = UserBase.objects.get(username=userinput)
    if user_filter:
        if user_filter.user_type == 1:
            return False
        return user_filter
    return False

def get_clients(user_id):
    # query = f"SELECT * FROM user_psychologist_clients WHERE user_psychologist_clients.psychologist_id={user_id}"
    psi = Psychologist.objects.get(user_id=user_id)
    
    clients = psi.clients.all()
    return clients

def get_all_forms_client(user_id):
    forms = Forms.objects.filter(user_id=user_id)
    # print(forms)
    # images = list(map(lambda x: x.img.path, forms))
    return forms