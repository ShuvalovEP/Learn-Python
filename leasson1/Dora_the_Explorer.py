# Пройдите в цикле по списку ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша'] пока не встретите имя 'Валера'. 
# Когда найдете напишите 'Валера нашелся'. Подсказка: используйте метод list.pop()

people_list = ['Ваня', 'Маша', 'Петя', 'Валера', 'Вася', 'Саша', 'Даша']

def dora(sought_man):
    while people_list:
        if people_list.pop() == sought_man:
            print('{name} нашелся!'.format(name=sought_man))
            break
        else:
            print('{name}, ты где?'.format(name=sought_man))

if __name__ == '__main__':
    dora('Валера')