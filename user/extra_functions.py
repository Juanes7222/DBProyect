import json
from .models import Forms

def get_questions():
    with open(r"C:\Users\juanb\Documents\Programacion\bdproject\user\questions.json", "r", encoding="utf-8") as file:
        quest = json.load(file)
    return quest.items()

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
    save_answers(score)
    
def save_answers(answers):
    
    Forms.objects.create(
        **answers
    )
    