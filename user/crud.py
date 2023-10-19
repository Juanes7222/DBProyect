from .models import UserBase, Psychologist, Forms

def get_info_user(user_id):
    user = UserBase.objects.get(id=user_id)
    query = f"SELECT * FROM user_psychologist_clients WHERE userbase_id={user_id}"
    integrations = Psychologist.clients.raw(query)
    data = {
        "user": user,
        "integrations": integrations
    }
    return data
