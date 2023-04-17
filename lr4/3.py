# Дан список чисел. Выполните следующие действия:
# а) Проверьте присутствие в нем числа -1. Если оно есть, выведите YES, в противном случае
# выведите NO.
# б) Найдите максимальный элемент.
# в) Вставьте число в начало списка.
# г) Удалите элемент с номером 5.
# д) Очистите список.

import random


lst = [random.randint(-10, 20) for i in range(10)] 

print('Исходный список:', lst)

print('Есть ли в списке -1?')
if -1 in lst:
    print("YES")
else:
    print("NO")
    
max_num = max(lst)
print("Максимальный элемент:", max_num)

lst.insert(0, -1)
print("Список после вставки:", lst)

del lst[4]
print("Список после удаления элемента с номером 5:", lst)

lst.clear()
print("Список после очистки:", lst)