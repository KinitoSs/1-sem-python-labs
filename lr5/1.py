# Напишите программу, которая по данному числу n от 1 до 9 выводит на экран n пингвинов.
# Изображение одного пингвина имеет размер 5×9 символов, между двумя соседними пингвинами также
# имеется пустой (из пробелов) столбец. Разрешается вывести пустой столбец после последнего пингвина.
# Для упрощения рисования скопируйте пингвина из примера. Учтите, что вывод данных на экран
# производится построчно, а не попингвинно.
# Пример пингвина:
#     _~_
#    (o o)
#    / V \
#   /( _ )\
#    ^^ ^^

amount = int(input('n = '))
p = "   _~_    "
e = "  (o o)   "
n = " /  V  \\  "
g = "/(  _  )\\ "
u = "  ^^ ^^   "
print(amount * p)
print(amount * e)
print(amount * n)
print(amount * g)
print(amount * u)