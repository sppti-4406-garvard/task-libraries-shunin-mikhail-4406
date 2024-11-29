from library import *


def main():
    library = []
    while True:
        print("\nСистема управления библиотекой:")
        print("1. Добавить книгу")
        print("2. Отобразить все книги")
        print("3. Найти книгу по названию")
        print("4. Удалить книгу")
        print("5. Выйти из программы")
        choice = input("Выберите действие (1-5): ").strip()

        if choice == "1":
            add_book(library)
        elif choice == "2":
            display_books(library)
        elif choice == "3":
            find_book(library)
        elif choice == "4":
            delete_book(library)
        elif choice == "5":
            print("Выход из программы. До свидания!")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
