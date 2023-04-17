# Найдите номер второго с конца отрицательного элемента списка. Если такого элемента нет,
# выведите -1.

lst = [1, 2, -3, 4, -5, 6, 7, -8]
negatives = [i for i in lst if i < 0]
if len(negatives) < 2:
    print(-1)
else:
    print(lst.index(negatives[-2]))