# Задача 1.1.

# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'
my_favorite_songs = my_favorite_songs.split(',')
print(my_favorite_songs)
# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.
len(my_favorite_songs)
print(my_favorite_songs[0] , end=' ')
print(my_favorite_songs[4] , end=' ')
print(my_favorite_songs[1] , end=' ')
print(my_favorite_songs[3])

 

# Comment of superviser:
# К сожалению, переопределять переменную my_favorite_songs нельяз по услвоию задачи!
# Постарайтесь перейти от строки my_favorite_songs к списку с помощью метода для строк!

#  UPDATED
