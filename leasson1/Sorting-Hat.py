#Sorting-Hat.py

input_age = input('Пожалуйста введите Ваш возраст: ')


def sorting_hat(age):
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
    convert_age = int(input_age) 
    return sorting_hat(convert_age)


def validation():
    if input_age.isdigit():
        convert()
    else:
        print('Возраст необходимо указать простым числом')
        pass


if __name__ == '__main__':
    validation()
