# Напишите программу, которая по номеру года определяет, является ли год високосным. Если год является високосным, то выведите ДА, иначе выведите НЕТ. 
# В соответствии с григорианским календарем год является високосным, если его номер кратен 4, но не кратен 100. Также високосным будет год, номер которого кратен 400.
year = int(input("Введите год: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("ДА")
else:
    print("НЕТ")
