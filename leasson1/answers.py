# answers.py

def get_answer():
    input_question = input("Скажи что-нибудь: ")
    answers = {'привет':'И тебе привет!', 'как дела':'Лучше всех!', 'пока':'Увидимся!'}
    return answers.get(input_question.lower())

if __name__ == '__main__':
    get_answer()