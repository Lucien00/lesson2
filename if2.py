def str_func(str1,str2):
    if type(str1)  and type(str2) != str:
        return '0'
    if str1 == str2:
        return '1'
    if str1 != str2 and len(str1) > len(str2):
        return '2'
    if str1 != str2 and str2 == 'learn':
        return '3'
print(str_func('hi',[1]))
print(str_func('hi','hi'))
print(str_func('hello','hi'))
print(str_func('hi','learn'))