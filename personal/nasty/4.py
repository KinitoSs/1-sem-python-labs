# задаем строку
s = "Это тестовая строка с 2 цифрами и 8 пробелами"

# инициализируем счетчики цифр и пробелов
digits = 0
spaces = 0

# перебираем символы в строке
for c in s:
  # если символ - цифра, увеличиваем счетчик цифр
  if c.isdigit():
    digits += 1
  # если символ - пробел, увеличиваем счетчик пробелов
  elif c == " ":
    spaces += 1

# выводим результаты
print(f"В строке {digits} цифр и {spaces} пробелов")