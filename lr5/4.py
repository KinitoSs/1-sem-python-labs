# Дана строка, состоящая из слов, разделенных пробелами. Определите количество слов в этой
# строке. Используйте метод count() для решения задачи.

string = "Это строка из нескольких слов"
print('Строка:', string)
word_count = string.count(" ") + 1
print("Количество слов в строке:", word_count)