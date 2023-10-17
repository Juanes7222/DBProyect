import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import json
import os
import locale
import zipfile
import io
from .models import Forms
from datetime import date, timedelta, datetime
from WheelofLife import settings
from django.http import FileResponse, HttpResponse


locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
matplotlib.use('Agg')  # Usa el backend 'Agg' (modo sin GUI)
media_directory = settings.MEDIA_ROOT
wheels_path = "wheels"


def get_questions():
    
    with open(os.path.join("user\static\questions.json"), "r", encoding="utf-8") as file:
        quest = json.load(file)
    return quest.items()

def generate_path_img_files(user_id, files, __path=f"static/img/media_users/{wheels_path}"):
    files = list(map(lambda x: os.path.join(__path, f"{user_id}/{x}"), files))
    return files

def path_normalize(files):
    new_path = list(map(lambda x: os.path.normpath(x), files))
    return new_path

def abs_path(files):
    new_path = list(map(lambda x: os.path.abspath(x), files))
    return new_path

def get_date_file(files):
    dates = []
    for file in files:
        file_date = date.fromisoformat(file.split("_")[-1][:-4])
        dates.append(file_date.strftime("%A, %d de %B de %Y"))
    return dates

def select_files(files: list[str], date):
    dates = []
    selected_files = []
    for file in files:
        file_date = date.fromisoformat(file.split("_")[-1][:-4])
        if  file_date >= date:
            selected_files.append(file)
            dates.append(file_date.strftime("%A, %d de %B de %Y"))
    return selected_files, dates

def get_files_folder(user_id, prov_date=None):
    try:
        path = f"{media_directory}/{wheels_path}/{user_id}"
        files = os.listdir(path)
        if prov_date == "all":
            return files, get_date_file(files)
        
        elif not prov_date:
            prov_date = date.today()
            prov_date -= timedelta(weeks=1)
        
        else:
            prov_date = date.fromisoformat(prov_date.split("T")[0])
            
        selected_files, dates = select_files(files, prov_date)
        return selected_files, dates
    except FileNotFoundError:
        return None

def form_manager(answers, user_id):
    score = get_answers(answers, user_id)
    form_id = save_answers(score)
    path = generate_image_path(user_id, form_id)
    values = list(score.values())
    values.pop()
    generate_wheel(values, path) 

def create_userfolder(user_id):
    new_path = os.path.join(media_directory, wheels_path, str(user_id))
    
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    return new_path

def get_answers(answers, user_id):
    quest = get_questions()
    score = {}
    for section, questions in quest:
        section = section.replace(" ", "_")
        list_score = []
        for question in questions:
            list_score.append(int(answers.get(question)))
        score[section] = sum(list_score) // len(list_score)
    score["user_id_id"] = user_id
    return score
    
    
def save_answers(answers):
    form = Forms.objects.create(
        **answers
    )
    return form.form_id
    
def generate_image_path(user_id, form_id):
    path = create_userfolder(user_id)
    specific_name = f"{user_id}_{form_id}_{date.today()}"
    image_path = f"{path}/{specific_name}.png"
    return image_path

def generate_color(blank_answers, colors, blank_colors):
    for i, b_answer in enumerate(blank_answers, 0):
        if b_answer == 0:
            blank_colors[i] = colors[i]
    blank_answers = map(lambda x: x+1, blank_answers)
    return list(blank_answers)
    

def generate_wheel(answers, image_path):

    # Datos para el diagrama circular exterior
    labels = ['Salud', 'Economia', 'Trabajo', 'Romance', 'Crecimiento personal', 'Amigos', 'Diversion', 'Imagen propia', "Ambiente físico"]
    length_labels = len(labels)
    sizes = [1, 1, 1, 1, 1, 1, 1, 1, 1]
    blank_answers = list(map(lambda x: x-10, answers))

    fig, ax = plt.subplots(figsize=(10, 10))
    # Número de círculos internos
    num_inner_circles = 10

    # Coordenadas para el centro de los círculos internos
    center_x, center_y = 0.5, 0.5

    colores = plt.cm.Paired(np.arange(length_labels))
    blank_colors = np.ones((length_labels, 4))

    inner_radius = 1
    border_color = 'black'
    ax.pie(sizes, startangle=90, radius=inner_radius, colors=colores, labels=labels,
            center=(center_x, center_y), wedgeprops={'edgecolor': border_color, 'linewidth': 0.5})
    ax.text(center_x, center_y+0.95, "10", horizontalalignment='center', verticalalignment='center', fontsize=13)
    ax.text(center_x+0.95, center_y, "10", horizontalalignment='center', verticalalignment='center', fontsize=13)
    ax.text(center_x, -1*center_y-0.95, "10", horizontalalignment='center', verticalalignment='center', fontsize=13)
    ax.text(-1*center_x-0.95, center_y, "10", horizontalalignment='center', verticalalignment='center', fontsize=13)

    for i in range(num_inner_circles):
        blank_answers = generate_color(blank_answers, colores, blank_colors)
        ax.pie(sizes, startangle=90, radius=inner_radius, colors=blank_colors,
            center=(center_x, center_y), wedgeprops={'edgecolor': border_color, 'linewidth': 0.5})
        ax.text(center_x, center_y+(i*0.1)+0.05, str(i+1), horizontalalignment='center', verticalalignment='center', fontsize=13)
        ax.text(center_x+(i*0.1)+0.05, center_y, str(i+1), horizontalalignment='center', verticalalignment='center', fontsize=13)
        ax.text(center_x, center_y-(i*0.1)-0.05, str(i+1), horizontalalignment='center', verticalalignment='center', fontsize=13)
        ax.text(center_x-(i*0.1)-0.05, center_y, str(i+1), horizontalalignment='center', verticalalignment='center', fontsize=13)
        inner_radius -= 0.1

    plt.savefig(image_path, dpi=600)
    
def download_zip(user_id, since_date):
    # Crear un objeto ZIP en memoria
    buffer = io.BytesIO()
    files = get_files_folder(user_id, since_date)[0]
    files = generate_path_img_files(user_id, files, f"{media_directory}/{wheels_path}")
    files = abs_path(files)
    files = path_normalize(files)
    # print(f"{files= }")
    with zipfile.ZipFile(buffer, 'a', zipfile.ZIP_DEFLATED) as zipf:
        # Agregar archivos al archivo ZIP
        for file in files:
            # El primer argumento es la ruta del archivo real, el segundo es la ruta dentro del ZIP
            print(f"path: {os.path.basename(file)}")
            zipf.write(file, os.path.basename(file))

    buffer.seek(0)
    # Configurar la respuesta HTTP
    response = HttpResponse(buffer.getvalue(), content_type='application/zip')
    file_name = f"{user_id}_{date.today().strftime('%Y-%m-%d')}.zip"  
    response['Content-Disposition'] = f'attachment; filename={file_name}'
    return response

def prueba():
    files = get_files_folder("1", "all")[0]
    files = generate_path_img_files("1", files, f"{media_directory}/{wheels_path}")
    files = abs_path(files)
    files = path_normalize(files)
    with zipfile.ZipFile('spam.zip', 'x') as myzip:
        for file in files:
            # El primer argumento es la ruta del archivo real, el segundo es la ruta dentro del ZIP
            print(f"path: {os.path.basename(file)}")
            myzip.write(file, os.path.basename(file))

prueba()
# def download_zip(user_id, since_date):
#     # Crea un objeto ZipFile
#     zip_file = zipfile.ZipFile()
#     files = get_files_folder(user_id, since_date)[0]
#     files = generate_path_img_files(user_id, files, f"{media_directory}/{wheels_path}")
#     files = abs_path(files)
#     files = path_normalize(files)
#     # Agrega archivos al archivo ZIP
#     for file in files:
#         print(os.path.basename(file))
#         zip_file.write(file, os.path.basename(file))

#     # Obtiene el archivo ZIP como un objeto BytesIO
#     buffer = io.BytesIO()
#     zip_file.writestr(buffer, 'archivo.zip')
#     zip_file.close()

#     # Devuelve el archivo ZIP como un objeto HttpResponse
#     response = HttpResponse(
#         buffer.getvalue(),
#         content_type='application/zip',
#         content_disposition='attachment; filename=archivo.zip'
#     )
    
#     return response