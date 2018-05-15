input_age = input('Пожалуйста введите Ваш возраст: ')


def sorting_hat(age):
    # Вызывается из convert() 
    # Принимает один аргумент age обязательно int()
    # Выводит сообщение в завистимсти от возраста
    if age <= 3:
        print('Еще совсем малыш')
    elif age > 3 and age <= 6:
        print('Учиться в детском саду')
    elif age > 6 and age <= 17:
        print('Учиться в школе')
    elif age > 17 and age <= 22:
        print('Учиться в ВУЗе')
    elif age > 22 and age <= 60:
        print('Работает')
    elif age > 60 and age <= 90:
        print('Пенсионер')
    elif age > 90 and age <= 121:
        print('Везучий человек')
    elif age >= 122:
        print('Здравствуйте Жанна Кальман')


def convert():
    # Вызывается из validation()
    # Конвертирует содержимое input_age в int()
    # Результат передается в виде аргумента в sorting_hat()
    convert_age = int(input_age) 
    return sorting_hat(convert_age)


def validation():
    # Проверяет является ли input_age числом
    # Вызывает функцию корвертации ввода в int()
    if input_age.isdigit():
        convert()
    else:
        print('Возраст необходимо указать простым числом')
        exit()


validation()