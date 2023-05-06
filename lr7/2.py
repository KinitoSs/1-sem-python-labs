n = int(input())  # считать количество городов
cities = set()  # создать пустой набор для хранения городов

# прочитать названия городов и добавьте их в набор
for i in range(n):
    city = input().strip()
    cities.add(city)

# прочитать название нового города
new_city = input().strip()

# проверить, был ли уже назван новый город
if new_city in cities:
    print("TRY ANOTHER")
else:
    print("OK")
