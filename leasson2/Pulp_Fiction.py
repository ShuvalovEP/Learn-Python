import csv

answers_dict = {'Привет': 'И тебе привет!', 'Как дела': 'Лучше всех', 
           'Пока': 'Увидимся', 'Как тебя зовут': 'Mr. Junked'}

with open ('answer.csv', 'w',  newline='') as file:
    write=csv.writer(file, delimiter=';')
    write.writerows(answers_dict.items())