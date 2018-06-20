#Class-Ratings.py

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
           {'school_class': '8v', 'scores': [5,2,2,4,2]}]


def average_score_class():
    class_average_scores = []
    for class_school in ratings: 
        average_scores = (sum(class_school['scores']) / len(class_school['scores']))
        class_average_scores.append(average_scores)
        print('Средний бал по классу: {} ='.format(class_school['school_class']), average_scores)
    print('Средний бал по школе: ', sum(class_average_scores, 1) / len(class_average_scores))


if __name__ == '__main__':
    average_score_class()
