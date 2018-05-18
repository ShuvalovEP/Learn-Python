# Написать функцию ask_user() чтобы с помощью input() спрашивать пользователя “Как дела?”, пока он не ответит “Хорошо”
def ask_user():
    while True: 
        answer = input('Как дела?')
        if answer == 'Хорошо':
            print('good')
            break

ask_user()


# При помощи функции get_answer() отвечать на вопросы пользователя в ask_user(),пока он не скажет “Пока!”
def get_answer(question):
    answers = {"Как дела": "Лучше всех", 
               "Сколько тебе лет": "31", 
               "Чем занимаешся": "Да ничем"}
    if question in answers:
        return answers.get(question)
    else:
        return 'Ты о чем?'


def ask_user():
    while True: 
        answer = input()
        if answer == 'Пока':
            print('Приятно было поболтать.')
            break
        else:
            print(get_answer(answer))
