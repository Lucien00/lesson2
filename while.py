
database = {'Как дела?': 'Хорошо', 'Что делаешь?': 'Отвечаю на вопросы',
            'На сколько вопросов можешь ответить?': '3'}

def ask_user():
    try:
        print('Задайте мне вопрос:')
        while True:
            answer = input()
            if database.get(answer):
                print(database[answer])
            else:
                print('Ответ на вопрос отсутствует')  

    except KeyboardInterrupt:
        print('Пока!') 
         

ask_user()


#def ask_user():
    #while True:
     #   user_say = input('Как дела? ')
      #  if user_say == 'Хорошо':
       #     break
#ask_user()
            
            