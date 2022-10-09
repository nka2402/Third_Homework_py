# <Задание 4>
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# Пример:
# 45 => 101101
# 3 => 11
# 2 => 10


def binary(number, answer=""):
    current = str(number % 2)
    number = number // 2
    if number > 0:
        answer += binary(number, answer)
    answer += str(current)
    return answer


num = int(input('Введите десятичное число: '))

print(f"{num} --> {binary(num)}")
