# С клавиатуры вводится строка, состоящая из нескольких слов, разделенных пробелами.
# Выполните следующие действия:
# а) Проверьте, содержится ли в строке буква а. Если да, выведите YES, иначе выведите NO.
# б) Найдите первое и последнее вхождения пробела в строку.
# в) Приведите строку к нижнему регистру.
# г) Удалите из строки все запятые.
# д) Разделите строку на слова.

# ввод строки
string = input("Введите строку: ")

# проверка на наличие буквы а
if 'а' in string.lower():
    print("YES")
else:
    print("NO")

# поиск первого и последнего пробела
first_space = string.find(' ')
last_space = string.rfind(' ')
print("Первый пробел:", first_space)
print("Последний пробел:", last_space)

# приведение строки к нижнему регистру
string = string.lower()
print("Строка в нижнем регистре:", string)

# удаление запятых
string = string.replace(',', '')
print("Строка без запятых:", string)

# разделение строки на слова
words = string.split()
print("Слова в строке:", words)