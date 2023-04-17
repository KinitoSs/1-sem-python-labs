# Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.

numbers = [1, 5, 2, 6, 3, 7, 4, 8]
result = []

for i in range(1, len(numbers)):
    if numbers[i] > numbers[i-1]:
        result.append(numbers[i])

print(result) # [5, 6, 7, 8]