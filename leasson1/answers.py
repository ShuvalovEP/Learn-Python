answers = {"Привет": "И тебе привет!", "Как дела": "Лучше всех", "Пока": "Увидимся"}
def get_answer(question):
    return answers.get(question.lower())
