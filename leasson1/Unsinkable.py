# Переписать функцию ask_user(), добавив обработку exception-ов
def get_answer(question):
    try:
        answers = {"Как дела": "Лучше всех", 
                   "Сколько тебе лет": "31", 
                   "Чем занимаешся": "Да ничем"}
        if question in answers:
            return answers.get(question)
        else:
            return 'Ты о чем?'
    except:
        return('Что то пошло не так')

def ask_user():
    try:
        answer = 0
        while True: 
            answer = input()
            if answer == 'Пока':
                print('Приятно было поболтать.')
                break
            else:
                print(get_answer(answer))
    except KeyboardInterrupt: # Добавить перехват ctrl+C и прощание
        print('Вы нажали сочетание клавиш: ctrl+c')
        exit()
