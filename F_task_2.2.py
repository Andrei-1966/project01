# Задача 2.2. 

# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.


user_input = input('Введите номер месяца:')

q_1 = {1:'январь', 2:'февраль', 3:'март'}
q_2 = {4:'апрель', 5:'май', 6:'июнь'}
q_3 = {7:'июль', 8:'август', 9:'сентябрь'} 
q_4 = {10:'октябрь', 11:'ноябрь', 12:'декабрь'}

month = int(user_input)

def quarter_of(month):  
    
    for month_k, month_n in q_1.items():
        if month == month_k:
            print('Месяц номер', month_k,'(', month_n,') является частью первого квартала', end='') 
    for month_k, month_n in q_2.items():
        if month == month_k:
            print('Месяц номер', month_k,'(', month_n,') является частью второго квартала', end='') 
    for month_k, month_n in q_3.items():
        if month == month_k:
            print('Месяц номер', month_k,'(', month_n,') является частью третьего квартала', end='') 
    for month_k, month_n in q_4.items():
        if month == month_k:
            print('Месяц номер', month_k,'(', month_n,') является частью четвертого квартала', end='')  
    return ''               

print(quarter_of(month))            