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


arr = [[4,6,2,1,9,63,-134,566],[-52, 56, 30, 29, -54, 0, -110],[42, 54, 65, 87, 0],[5]]

n = len(arr[0])
#print(n)
#print(arr[0])
x = arr[0]
#print(x)

for i in range(n-1):
  for j in range(n-i-1):
    if x[j] > x[j+1]:
     x[j], x[j+1] = x[j+1], x[j] 
print('в массиве',arr[0] , ' -> min = ',x[0],'max =', x[7])   

n =len(arr[1])
h = arr[1]
#print(h)
for i in range(n-1):
  for j in range(n-i-1):
   if h[j] > h[j+1]:
     h[j], h[j+1] = h[j+1], h[j]             
print('в массиве',arr[1], ' -> min = ',h[0],'max =',h[6]) 

n = len(arr[2])
z = arr[2]
#print(z)   
for i in range(n-1):
  for j in range(n-i-1):
    if z[j] > z[j+1]:
     z[j], z[j+1] = z[j+1], z[j]             
print('в массиве',arr[2], ' -> min = ',z[0],'max =',z[4]) 

k = arr[3]
#print(k)              
print('в массиве',arr[3], ' -> min = ',k[0],'max =',k[0]) 