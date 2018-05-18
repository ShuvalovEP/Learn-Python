
people_list = ["Ваня", "Маша", "Петя", "Валера", "Вася", "Саша", "Даша"]


def find_person(name):
    for person in people_list:
        if person == name:
            print('{find_name} под номером: '.format(find_name = name), people_list.index(person))


find_person("Вася")
