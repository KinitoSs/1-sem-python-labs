# Проходим циклом по числам от 1 до 200
for i in range(1, 201):
    # Если число делится на 4 и на 7 без остатка, выводим его на экран
    if i % 4 == 0 and i % 7 == 0:
        print(i)
