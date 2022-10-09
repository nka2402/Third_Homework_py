#<Задание 5>
#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
#Пример:
#для num = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
# (Негафибоначчи)

num = int(input('Введите число: '))

arr = [0, 1]
for i in range(2, num):
    arr.append(arr[i - 1] + arr[i - 2])

print(arr)

result = []
length = len(arr) - 1
for i in range(length):
    if i % 2 == 0:
        num = 1
    else:
        num = -1
    result.append(arr[length - i] * num)
result = result + arr

print(result)