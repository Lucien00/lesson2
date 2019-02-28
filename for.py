import numpy as np

students_scores = [
    {'school_class': '5a', 'scores': [4,4,5,3,5]},
    {'school_class': '5b', 'scores': [3,4,3,3,5]},
    {'school_class': '5c', 'scores': [5,2,4,4,4]},
    {'school_class': '5d', 'scores': [5,5,5,4,5]}
    ]
    
sum_mean = 0
for classes in students_scores:
    mean_score_classes = np.mean(classes['scores'])
    print('Cредний балл по классу', classes['school_class'],':', mean_score_classes)

    sum_mean += mean_score_classes
    mean_score_school = round(sum_mean/len(students_scores), 1)
print('Cредний балл по всей школе : ', mean_score_school)