# Вводим два объема с клавиатуры
v1 = float(input("Введите объем в кубических метрах: "))
v2 = float(input("Введите объем в литрах: "))

# Переводим объем в литрах в кубические метры
v2 = v2 / 1000

# Сравниваем два объема
if v1 < v2:
    print("Объем в кубических метрах меньше")
elif v1 > v2:
    print("Объем в литрах меньше")
else:
    print("Объемы равны")