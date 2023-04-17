# Найти НОД (наибольший общий делитель) двух введенных чисел m и
# n. Для нахождения НОД используется следующий вариант алгоритма Евклида:
# 1. Если числа равны, алгоритм останавливается;
# 2. Если первое число больше второго, то из первого вычитаем второе и
# возвращаемся к пункту 1
# 3. Если второе число больше первого, то из второго вычитаем первое и
# возвращаемся к пункту 1.

m = int(input("Введите первое число: "))
n = int(input("Введите второе число: "))

while m != n:
    if m > n:
        m = m - n
    else:
        n = n - m

print("НОД равен", m)