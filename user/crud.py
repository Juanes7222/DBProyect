from .models import UserBase, Psychologist, Forms
from .forms import CreateNewUser


def get_info_user(user_id):
    user = UserBase.objects.get(id=user_id)
    query = f"SELECT * FROM user_psychologist_clients WHERE userbase_id={user_id}"
    integrations = Psychologist.clients.raw(query)
    data = {
        "user": user,
        "integrations": integrations
    }
    return data

def save_answers(answers):
    form = Forms.objects.create(
        **answers
    )
    return form

def save_integrate(user_id, psi_id):
    psi = Psychologist.objects.get(user_id=psi_id)
    user = UserBase.objects.get(id=user_id)
    if psi.clients.get(id=user_id):
        return False
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