# Вычислите сумму квадратов чисел от 1 до m: 1^2 + 2^2 + ⋯ + 𝑚^2.
# Сложение продолжайте до тех пор, пока сумма чисел не превысит числа n, вводимого
# с клавиатуры.

m = int(input("Введите число m: "))
n = int(input("Введите число n: "))

sum_of_squares = 0

i = 1
while sum_of_squares <= n:
    sum_of_squares += i**2
    i += 1

sum_of_squares -= i**2

print("Сумма квадратов чисел от 1 до", m, "равна", sum(i**2 for i in range(1, m + 1)))
print("Сумма квадратов чисел от 1 до", i - 1, "равна", sum_of_squares)
