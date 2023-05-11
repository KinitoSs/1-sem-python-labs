# создаем словарь, где ключ - месяц, значение - список имен именинников
birthdays = {}
# считываем количество одноклассников
n = int(input())
# считываем информацию о каждом однокласснике и заполняем словарь
for i in range(n):
    name, day, month = input().split()
    if month not in birthdays:
        birthdays[month] = []
    birthdays[month].append(name)
# считываем месяц, для которого нужно вывести имена именинников
search_month = input()
# выводим имена именинников, родившихся в заданном месяце
print(" ".join(birthdays.get(search_month, [])))
