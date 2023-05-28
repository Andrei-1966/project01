# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)


import sqlite3

connection = sqlite3.connect('teatchers.db')
cursor = connection.cursor()
sqlquery = """ CREATE TABLE Students (
Student_Id INTEGER NOT NULL, 
Student_Name TEXT NOT NULL,
School_Id INTEGER NOT NULL PRIMARY KEY
); 
"""
#cursor.execute(sqlquery)  # is commited for next code working  
connection.commit()
connection.close()

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4


connection = sqlite3.connect('teatchers.db')
cursor = connection.cursor()
sqlquery = """ INSERT INTO Students ( Student_Id, Student_Name, School_Id)
VALUES
(201, 'Иван', 1),
(202, 'Петр', 2),
(203, 'Анастасия', 3),
(204, 'Игорь', 4);"""
#cursor.execute(sqlquery)  # is commited for next code working  
connection.commit()
connection.close()


# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:



def get_connection():
    connection = sqlite3.connect('teatchers.db')
    return connection

def close_connection(connection):
    if connection:
        connection.close()
 

def get_students_info(student_id):        
    try:
        school_name = 'High school'
        connection = get_connection()
        cursor = connection.cursor() 
        select_query = "SELECT * FROM Students WHERE Student_Id = ?"
        cursor.execute(select_query,(student_id,))
        record = cursor.fetchall()
        close_connection(connection)
        print ('Студенты из школы', school_name)
        for row in record:
            print(' ID Студента:', row[0])
            print(' Имя Студента:', row[1])
            print(' ID школы:', row[2])  
            print(' Название школы:', school_name)        
        close_connection(connection)

    except (Exception, sqlite3.Error) as error:
        print (' Ошибка в получении данныхЖ', error)        

x = int(input('Введи ID:')) 

get_students_info(x)        