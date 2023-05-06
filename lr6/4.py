def tribonacci(n):
    # определяем начальные значения
    a, b, c = 0, 0, 1

    # вычисляем числа Трибоначчи до n-го числа
    for i in range(n):
        a, b, c = b, c, a + b + c

    # возвращаем n-ое число Трибоначчи
    return a


print(tribonacci(0))  # 0
print(tribonacci(1))  # 0
print(tribonacci(2))  # 1
print(tribonacci(3))  # 1
print(tribonacci(4))  # 2
print(tribonacci(5))  # 4
