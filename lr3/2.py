# Напечатайте таблицу умножения на число N, учитывая, что значение N вводится с клавиатуры, 
# и его значение находится в диапазоне от 1 до 10 включительно. Ответ должен выводиться 
# пользователю в виде набора примеров 1 ∗ 8 = 8.

n = int(input("Введите число от 1 до 10: "))

for i in range(1, 11):
    print(f"{i} * {n} = {i*n}")