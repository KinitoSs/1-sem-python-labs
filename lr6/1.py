def sum_range(start, end):
    # Проверяем, если первое число больше второго, то меняем их местами
    if start > end:
        start, end = end, start

    # Используем встроенную функцию sum() для суммирования чисел
    # Функция range() создает последовательность чисел от start до end + 1
    # В результате получаем сумму чисел от start до end включительно
    return sum(range(start, end + 1))


print(sum_range(1, 5))
