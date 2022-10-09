#<Задание 2>
#Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

#Пример:
#[2, 3, 4, 5, 6] => [12, 15, 16]
#[2, 3, 5, 6] => [12, 15]

import random

arr = []
n = int(input('Введите размер массива: '))
for i in range(n):
    arr.append(random.randint(1,10))
print(arr)

result = []

for i in range(0, int((len(arr) + 1) / 2)):
    multi = arr[i] * arr[len(arr)-i-1]
    result.append(multi)

print(result)


    







