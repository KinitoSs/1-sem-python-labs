# Напишите программу, которая анализирует человека по возрасту и относит к
# одной из пяти групп: дошкольник, школьник, студент, работник, пенсионер.
# Возраст человека вводится с клавиатуры. Возрастные границы определить самостоятельно.
age = int(input("Введите возраст: "))

if age < 7:
    print("Вы дошкольник")
elif age < 18:
    print("Вы школьник")
elif age < 23:
    print("Вы студент")
elif age < 60:
    print("Вы работник")
else:
    print("Вы пенсионер")
