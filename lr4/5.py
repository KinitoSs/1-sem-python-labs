# Замените все нулевые элементы целочисленного списка на случайно сгенерированные
# ненулевые элементы.

import random

lst = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5]

print(lst)

for i in range(len(lst)):
    if lst[i] == 0:
        lst[i] = random.randint(1, 100)

print(lst)
