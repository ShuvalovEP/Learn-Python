ratings = [{'school_class': '5a', 'scores': [2,3,5,2,5]},
           {'school_class': '6a', 'scores': [3,4,4,3,4]},
           {'school_class': '7a', 'scores': [4,5,3,2,3]},
           {'school_class': '8a', 'scores': [5,2,2,3,2]},
           {'school_class': '5b', 'scores': [2,3,5,2,5]},
           {'school_class': '6b', 'scores': [3,4,4,4,4]},
           {'school_class': '7b', 'scores': [4,5,3,3,3]},
           {'school_class': '8b', 'scores': [5,2,2,2,2]},
           {'school_class': '5v', 'scores': [2,3,5,5,5]},
           {'school_class': '6v', 'scores': [3,4,4,4,4]},
           {'school_class': '7v', 'scores': [4,5,3,3,3]},
           {'school_class': '8v', 'scores': [5,2,2,4,2]}
           ]

# Посчитать и вывести средний балл по каждому классу.   

def average_score_class():
    id = 0 
    for school_class in ratings: 
        count_score = 0
        len_scores = len(school_class['scores'])
        for scores in school_class['scores']:
            count_score += scores
            ratings[id]['count_score'] = count_score / len_scores
        id += 1
        print('Класс: ', school_class['school_class'], 'Средний бал: ', school_class['count_score'])


average_score_class()

#Посчитать и вывести средний балл по всей школе.
