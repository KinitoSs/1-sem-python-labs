# вводим количество книг в домашней библиотеке
num_books_library = int(input())
# создаем пустое множество для хранения книг
books_library = set()
for i in range(num_books_library):
    # вводим название книги
    book = input().strip()
    # добавляем книгу в множество
    books_library.add(book)

# вводим количество книг в списке летнего чтения
num_books_summer = int(input())
# создаем пустой список для хранения книг
books_summer = []
for i in range(num_books_summer):
    # вводим название книги
    book = input().strip()
    # добавляем книгу в список
    books_summer.append(book)

for book in books_summer:
    # проверяем наличие книги в домашней библиотеке
    if book in books_library:
        print("YES")
    else:
        print("NO")
