

def get_answer(question):
    answers = {"Как дела": "Лучше всех", 
               "Сколько тебе лет": "31", 
               "Чем занимаешся": "Да ничем"}
    return answers.get(question, 'Ты о чём?')


def ask_user():
    try:
        while True: 
            answer = input()
            if answer == 'Пока':
                print('Приятно было поболтать.')
                break
            else:
                print(get_answer(answer))
    except KeyboardInterrupt:
        print('Вы нажали сочетание клавиш: ctrl+c')
        exit()
