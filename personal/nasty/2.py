# Создаем цикл для переменной i от 1 до 200 включительно
for i in range(1, 201):
    # Проверяем, что i делится нацело и на 4, и на 7
    if i % 4 == 0 and i % 7 == 0:
        print(i)  # Выводим i на экран
