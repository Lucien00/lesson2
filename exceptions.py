def get_summ(num_one, num_two):
    try:
        return int(num_one) + int(num_two)
    except ValueError:
        return 'Введите другие числа'
sum = get_summ(9, '2.3')        
print(sum)  