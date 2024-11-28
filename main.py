from Library import Library, Book


def main() -> None:
    library = Library()

    while True:
        print('\nМеню')
        print('1. Добавить книгу')
        print('2. Удалить книгу')
        print('3. Найти книгу')
        print('4. Отобразить все книги')
        print('5. Изменить статус книги')
        print('6. Выйти')

        choice = input('Выберите действие: ')

        if choice == '1':
            title = input('Введите название книги: ')
            author = input('Введите автора: ')
            year = input('Введите год издания: ')
            if not year.isdigit():
                print('Год издания должен быть числом')
                continue
            book = Book(title, author, int(year))
            library.add_book(book)

        elif choice == '2':
            book_id_input = input('Введите ID книги для удаления: ')
            if not book_id_input.isdigit():
                print('ID должен быть числом')
                continue
            book_id = int(book_id_input)
            library.remove_book(book_id)

        elif choice == '3':
            print('Поиск книг по названию, автору или году издания')
            title_book = input('Название: ')
            author_book = input('Автор: ')
            book_year = input('Год издания: ')
            if book_year:
                book_year = int(book_year)
            library.find_book(title_book, author_book, book_year)

        elif choice == '4':
            library.display_books()

        elif choice == '5':
            book_id_input = input('Введите ID для изменения статуса: ')
            if not book_id_input.isdigit():
                print('ID должен быть числом')
                continue
            book_id = int(book_id_input)
            library.display_status(book_id)
            new_status = input('Введите новый статус (в наличии/выдана): ')
            library.change_status(book_id, new_status)

        elif choice == '6':
            print('Выход из программы')
            break

        else:
            print('Неверный выбор. Выберите действие от 1 до 6')


if __name__ == '__main__':
    main()
