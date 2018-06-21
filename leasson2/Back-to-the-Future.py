#Back-to-the-Future.py
from datetime import timedelta, datetime

delta_list = {'yesterday': timedelta(days=1), 'month_ago': timedelta(
    weeks=4), 'now_day': datetime.now()}
date_string = '01/01/17 12:10:03.234567'


def date_string(args):
    args = args.strftime('%d.%m.%y')
    return args


def delta_date(args):
    date_delta = delta_list.get(args)
    get_now_day = delta_list.get('now_day')
    calculation_time = get_now_day - date_delta
    convert = date_string(calculation_time)
    return convert


def transformation_date(args):
    transformation = datetime.strptime(args, '%d/%m/%y %H:%M:%S.%f')
    return transformation


def today():
    date = delta_list.get('now_day')
    convert = date_string(date)
    return convert


def main():
    try:
        while True:
            print('\n Нажмите 1 - Вчера\n'
                  ' Нажмите 2 - Сегодня\n'
                  ' Нажмите 3 - Месяц назад\n'
                  ' Нажмите 4 - Преобразовать: 01/01/17 12:10:03.234567'
                  )
            print(' \n Для выхода нажмите ctrl+c')
            command = input(' Введите номер команды: ')
            if command == '1':
                print('\n Вчера было:', delta_date('yesterday'))
            elif command == '2':
                print('\n Сегодня:', today())
            elif command == '3':
                print('\n Месяц назад:', delta_date('month_ago'))
            elif command == '4':
                print('\n Преобразовано в datetime:',
                      transformation_date(date_string))
            else:
                print('{} - команда обязательно должна быть числом'.format(command))
    except KeyboardInterrupt:
        print('\n   Пока, пока!')


if __name__ == '__main__':
    main()
