#Pulp_Fiction.py
import csv

answers_dict = {'Привет': 'И тебе привет!', 'Как дела': 'Лучше всех',
                'Пока': 'Увидимся', 'Как тебя зовут': 'Mr. Junked'}

def csv_writer():
    with open('answer.csv', 'w',  newline='') as file:
        write = csv.writer(file, delimiter=';')
        write.writerows(answers_dict.items())


if __name__ == '__main__':
    csv_writer()
