import json

def get_questions():
    with open(r"C:\Users\juanb\Documents\Programacion\bdproject\user\questions.json", "r", encoding="utf-8") as file:
        quest = json.load(file)
    questions =  {"quests": quest.items()}
    return questions

def save_answers(answers):
    ...