# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

print('Задача 1.2', ' Пункт A')
import random
list = random.sample(my_favorite_songs, 3)
print(list)
total_time = 0
for name, time in list:
    print(f'трек {name} - {time} минут')
    total_time += time
print(f'Три песни звучат - {total_time} минут')
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')


# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

print('Задача 1.2' , 'Пункт B')
import random 
list = my_favorite_songs_dict
for name, time in list.items():
   # print([name, time]) => copy result from terminal and update the list with "," between []
    list = [         
['Waste a Moment', 3.03],
['New Salvation', 4.02],
["Staying' Alive", 3.4],
['Out of Touch', 3.03],
['A Sorta Fairytale', 5.28],
['Easy', 4.15],
['Beautiful Day', 4.04],
['Nowhere to Run', 2.58],
['In This World', 4.02],]    
   # print(list)
list = random.sample(list, 3)
print(list)
total_time = 0
for name, time in list:
    print(f'трек {name} - {time} минут')
    total_time += time
print(f'Три песни звучат - {total_time} минут')
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
 
    

 

  
  
 
   





 


# Дополнительно для пунктов A  и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

