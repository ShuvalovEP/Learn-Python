# Перепишите предыдущий пример в виде функции find_person(name), которая ищет имя в списке.
people_list = ["Ваня", "Маша", "Петя", "Валера", "Вася", "Саша", "Даша"]
def find_person(name):
    for person in people_list:
        if person == name:
            print(person, 'под номером: ', people_list.index(person))


find_person("Вася")
