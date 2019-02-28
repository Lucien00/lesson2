age = int(input())

def activity(age):
    if 2 <= age < 7:
        return 'Иди в детский сад'
    elif 7 <= age < 18:
        return 'Иди в школу'
    elif 18 <= age <= 24:
        return 'Иди в ВУЗ'
    elif 24 < age <= 65:
        return 'Иди на работу'
    
act = activity(age)
print(act)




