# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!

def minimum(arr):
    pass

def maximum(arr):
    pass

#UPDATED Version
#arr = [[4,6,2,1,9,63,-134,566],[-52, 56, 30, 29, -54, 0, -110],[42, 54, 65, 87, 0],[5]]

# List #1
arr = [4,6,2,1,9,63,-134,566]
n = len(arr)
x = arr
def minimum(x):
    for i in range(n-1):
     for j in range(n-i-1):
       if x[j] > x[j+1]:
          x[j], x[j+1] = x[j+1], x[j] 
    return x[0]
def maximum(x):
    for i in range(n-1):
     for j in range(n-i-1):
       if x[j] > x[j+1]:
        x[j], x[j+1] = x[j+1], x[j] 
    return x[7]

print('в массиве',arr , ' -> min = ', minimum(x),'max =', maximum(x))   

# List #2
arr2 =[-52, 56, 30, 29, -54]
n = len(arr2)
x = arr2
def minimum(x):
    for i in range(n-1):
     for j in range(n-i-1):
       if x[j] > x[j+1]:
          x[j], x[j+1] = x[j+1], x[j] 
    return x[0]
def maximum(x):
    for i in range(n-1):
     for j in range(n-i-1):
       if x[j] > x[j+1]:
        x[j], x[j+1] = x[j+1], x[j] 
    return x[4]

print('в массиве',arr2 , ' -> min = ', minimum(x),'max =', maximum(x))   

# List #2
arr3 =[42, 54, 65, 87, 0]
n = len(arr3)
x = arr3
def minimum(x):
    for i in range(n-1):
     for j in range(n-i-1):
       if x[j] > x[j+1]:
          x[j], x[j+1] = x[j+1], x[j] 
    return x[0]
def maximum(x):
    for i in range(n-1):
     for j in range(n-i-1):
       if x[j] > x[j+1]:
        x[j], x[j+1] = x[j+1], x[j] 
    return x[4]

print('в массиве',arr3 , ' -> min = ', minimum(x),'max =', maximum(x))   

# List #4
arr4 =[5]
n = len(arr4)
x = arr4
def minimum(x):
    for i in range(n-1):
     for j in range(n-i-1):
       if x[j] > x[j+1]:
          x[j], x[j+1] = x[j+1], x[j] 
    return x[0]
def maximum(x):
    for i in range(n-1):
     for j in range(n-i-1):
       if x[j] > x[j+1]:
        x[j], x[j+1] = x[j+1], x[j] 
    return x[0]

print('в массиве',arr4 , ' -> min = ', minimum(x),'max =', maximum(x))   