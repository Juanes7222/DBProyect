import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.use('Agg')  # Usa el backend 'Agg' (modo sin GUI)


def generate_codes():
    ...

def generar_rueda_de_vida():
    # Áreas de la vida y sus puntuaciones (ejemplo)
    areas = ['Salud', 'Relaciones', 'Carrera', 'Finanzas', 'Familia', 'Amigos', 'Tiempo libre', 'Crecimiento personal']
    puntuaciones = [7, 8, 6, 5, 9, 7, 6, 8]

    # Crear una figura
    fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})

    # Colores para cada área
    colores = plt.cm.Paired(np.arange(len(areas)))

    # Dibujar un gráfico de pastel con puntuaciones
    ax.pie(puntuaciones, labels=areas, colors=colores, autopct='%1.1f%%')

    # Agregar un círculo blanco en el centro (simulando el centro de la rueda)
    centro_circulo = plt.Circle((0, 0), 0.70, fc='white')
    fig.gca().add_artist(centro_circulo)

    # Personalizar el aspecto de la rueda
    ax.axis('equal')  # Proporciones iguales para que parezca una rueda
    plt.title('Rueda de la Vida')

    # Guardar la imagen
    imagen_path = './hola.png'
    plt.savefig(imagen_path)
    
# generar_rueda_de_vida()


# Nota idea: para generar la rueda se puede simplemente generar circulos (10 por el mayor puntaje) y se va pintando de esa seccion dependiendo de la puntuacion en esa area (ver imagen example1.)