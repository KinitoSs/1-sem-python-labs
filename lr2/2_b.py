# Найдите максимальное и минимальное значения из двух целых чисел, введенных с клавиатуры.
# Если два числа равны, в качестве максимального и минимального можно брать любое из них, то есть
# минимальное и максимальное будут всегда. Решите задачу двумя способами:
# б) в решении нельзя использовать функции из библиотеки math.

x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))

if x > y:
    max_value = x
    min_value = y
else:
    max_value = y
    min_value = x

print("Максимальное значение:", max_value)
print("Минимальное значение:", min_value)
