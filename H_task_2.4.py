# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"
users_input = input(str('Remove all em signes form your input:'))
def remove_exclamation_marks(s):
#    pass 
    s = users_input
    return users_input.replace('!','')
print(f'foo (',users_input,') --> "',remove_exclamation_marks(users_input),'"')


# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

users_input = input(str('Remove the last em signe form your input:'))
def remove_last_em(s):
#    pass 
   s = users_input 
   return users_input[:-1]
print(f'Remove from ("',users_input,'") == "', remove_last_em(users_input),'"')


# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

users_input = input(str('Remove all words with one em signe form your input:'))
def remove_word_with_one_em(s):
#   pass
    s = users_input
    return' '.join(w for w in users_input.split() if w.count('!') != 1 )
print(f'remove from ("',users_input,'") == "',remove_word_with_one_em(users_input),'"')


    