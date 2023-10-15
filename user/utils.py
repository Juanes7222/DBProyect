import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import json
import os
from .models import Forms
from datetime import date

matplotlib.use('Agg')  # Usa el backend 'Agg' (modo sin GUI)

def get_questions():
    
    with open(os.path.join("user\static\questions.json"), "r", encoding="utf-8") as file:
        quest = json.load(file)
    return quest.items()

def get_files_folder(user_id, date=None):
    path = "user/static/img/wheels"
    try:
        files = os.listdir(f"{path}/{user_id}") 
        return files
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
    path = "user/static/img/wheels"
    new_path = os.path.join(path, str(user_id))
    
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
# plt.show()
# generate_wheel([1, 3, 5, 6, 5, 3, 7, 8, 4], "./hola.png")
# generar_rueda_de_vida()


# Nota idea: para generar la rueda se puede simplemente generar circulos (10 por el mayor puntaje) y se va pintando de esa seccion dependiendo de la puntuacion en esa area (ver imagen example1.)