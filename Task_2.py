# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random

minn = int(input('Задайте минимум: '))
maxx = int(input('Задайте максимум: '))

my_list = [random.randint(-100, 100) for _ in range(int(input('Введите количество элементов массива: ')))]
print(my_list)

result = [i for i in range(len(my_list)) if minn < my_list[i] < maxx]
print(f' Индексы элементов, значения которых в диапазоне от {minn} до {maxx}, равны: {result}')

