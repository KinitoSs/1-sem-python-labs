# Создаем пустой словарь для хранения фамилий и их количества
families = {}

# Получаем список фамилий от пользователя
surname_list = input("Введите список фамилий через пробел: ").split(" ")

# Перебираем каждую фамилию в списке
for surname in surname_list:
    # Если фамилия уже есть в словаре, увеличиваем ее количество на 1
    if surname in families:
        families[surname] += 1
    # Если фамилии нет в словаре, добавляем ее и устанавливаем количество на 1
    else:
        families[surname] = 1

# Выводим результат
print("Результат:")
for surname, count in families.items():
    print(f"{surname}: {count}")