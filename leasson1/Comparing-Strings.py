#Comparing-Strings.py


def comp_str(str1, str2):
    # принимаем два аргумента
    if str1 == str2:
        return 1
    else: # если строки не равны проверям остальные условия
        if len(str1) > len(str2):
            return 2
        elif str2 == 'learn':
            return 3
        else: 
            print('Исключительная ситуация', str1, str2)


if __name__ == '__main__':
    comp_str('learn', 'learn')
    comp_str('learn1', 'learn')
    comp_str('1', 'learn')