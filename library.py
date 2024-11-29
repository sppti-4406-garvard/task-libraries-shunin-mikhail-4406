def add_book(library):
    title = input("Введите название книги: ").strip()
    author = input("Введите автора книги: ").strip()
    while True:
        try:
            year = int(input("Введите год издания книги: "))
            break
        except ValueError:
            print("Год должен быть числом. Попробуйте снова.")
    library.append({"название": title, "автор": author, "год": year})
    print("Книга успешно добавлена!")


def display_books(library):
    if not library:
        print("Библиотека пуста.")
        return
    print("Список книг в библиотеке:")
    for idx, book in enumerate(library, 1):
        print(f"{idx}. {book['название']} — {book['автор']} ({book['год']})")


def find_book(library):
    query = str(input("Введите название книги для поиска: "))
    found_books = [book for book in library if query == book["название"]]
    if found_books:
        print("Найдены следующие книги:")
        for idx, book in enumerate(found_books, 1):
            print(f"{idx}. {book['название']} — {book['автор']} ({book['год']})")
    else:
        print("Книга не найдена.")


def delete_book(library):
    query = input("Введите название книги для удаления: ").strip()
    for book in library:
        if book["название"].lower() == query.lower():
            library.remove(book)
            print("Книга успешно удалена!")
            return
    print("Книга с таким названием не найдена.")