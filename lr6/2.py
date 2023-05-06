def nod(a, b):
    if a == b:
        return a
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


print(nod(10, 5))
