# Напишите программу, выясняющую, четным или нечетным
# является введенное с клавиатуры целое число. Ноль считать четным.

num = int(input("Введите целое число: "))

if num % 2 == 0:
    print("Число", num, "является четным")
else:
    print("Число", num, "является нечетным")
