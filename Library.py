import json


class Book:
    """Класс представляющий книгу в библиотеке"""

    def __init__(self, title: str, author: str, year: int):
        self.id = None
        self.title = title
        self.author = author
        self.year = year
        self.status = 'в наличии'  # статус книги по умолчанию

    def __str__(self) -> str:
        # Возвращает строковое представление книги
        return f'\nназвание: {self.title}\nАвтор: {self.author}\nгод издания: {self.year}\nстатус: {self.status}'


class Library:
    """Класс определяющий основные функции которые можно выполнять с книгами"""

    def __init__(self):
        self.books = []
        self.id = 1
        self.load_books()

    def load_books(self) -> None:
        # Загружает список словарей представляющих книги из файла Library.json
        try:
            with open('Library.json', encoding='utf-8') as file:
                books_data = json.load(file)
                for book_dict in books_data:
                    book = Book(
                        book_dict['title'],
                        book_dict['author'],
                        book_dict['year']
                    )
                    book.id = book_dict['id']
                    book.status = book_dict['status']
                    self.books.append(book)
                    if book.id >= self.id:
                        self.id += book.id
        except FileNotFoundError:
            print('Файл библиотеки не найден, библиотека пуста')

    def save_books(self) -> None:
        # Сохраняет список книг в файл Library.json
        books_data = [book.__dict__ for book in self.books]
        with open('Library.json', 'w', encoding='utf-8') as file:
            json.dump(books_data, file, indent=4)

    def add_book(self, book) -> None:
        # Функция для добавления книги в библиотеку
        book.id = self.id
        self.id += 1
        self.books.append(book)
        self.save_books()
        print(f'Книга {book.title} добавлена в библиотеку')

    def remove_book(self, book_id: int) -> None:
        # Удаляет книгу по указанному ID
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                self.save_books()
                print(f'Книга {book.title}, ID: {book_id} удалена из библиотеки')
        print(f'Книга с ID: {book_id} не найдена')

    def find_book(self, title=None, author=None, year=None) -> None:
        # Функция осуществляет поиск книг по названию, автору или году
        if title:
            for book in self.books:
                if book.title == title:
                    print(f'Книга {title} найдена\nАвтор: {book.author}')
                    return
            print(f'Ни одной книги с названием {title} не найдено')
        elif author:
            print(f'Книги автора: {author}\n')
            found = False
            for book in self.books:

                if book.author == author:
                    print(f'{book.title}, год: {book.year}\n ')
                    found = True
            if not found:
                print(f'Ни одной книги автора {author} не найдено')
        elif year:
            print(f'Книги {year} года издания\n')
            found = False
            for book in self.books:
                if book.year == year:
                    print(f'{book.title}, автор: {book.author}\n ')
                    found = True
            if not found:
                print(f'Ни одной книги {year} года издания не найдено')

    def display_books(self) -> None:
        # Функция для отображения всего списка книг
        if not self.books:
            print('Библиотека пуста')
        else:
            for book in self.books:
                print(book)

    def display_status(self, book_id: int) -> None:
        # Функция для отображения текущего статуса
        for book in self.books:
            if book.id == book_id:
                print(f'Текущий статус: {book.status}')

    def change_status(self, book_id: int, new_status: str):
        # Функция для изменения текущего статуса
        for book in self.books:
            if book.id == book_id:
                book.status = new_status
                self.save_books()
                print(f'Статус книги изменен на: {new_status}')
                return
        print(f'Книга с ID:{book_id} не найдена')
