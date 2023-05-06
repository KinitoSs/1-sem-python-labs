# Создаем пустой словарь для хранения количества вхождений каждого символа
count_dict = {}

# Получаем текст от пользователя
text = input()

# Переводим текст в верхний регистр
text = text.upper()

# Итерируемся по каждому символу в тексте
for char in text:
    # Если символ уже встречался, увеличиваем его счетчик на 1
    if char in count_dict:
        count_dict[char] += 1
    # Если символ встречается впервые, добавляем его в словарь со счетчиком 1
    else:
        count_dict[char] = 1

# Сортируем ключи словаря в лексикографическом порядке
sorted_keys = sorted(count_dict.keys())

# Итерируемся по каждому символу в отсортированном списке ключей
for char in sorted_keys:
    # Выводим символ и количество его вхождений, разделенные тире
    print(char, "-", count_dict[char])
