#<Задание 1>
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] => на нечётных позициях элементы 3 и 9, ответ: 12

import random

arr = []
n = int(input('Введите размер массива: '))
for i in range(n):
    arr.append(random.randint(0,50))
print(arr)
result = 0
for i in range(len(arr)):
    if i%2!=0:
        result = result+arr[i]
    else:
        result = result

print(f'Сумма чисел на нечетных позициях = {result}')