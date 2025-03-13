BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    """
    Класс, представляющий книгу.
    """

    def __init__(self, id_: int, name: str, pages: int):
        """
        Конструктор класса Book.

        Args:
            id_: Идентификатор книги.
            name: Название книги.
            pages: Количество страниц в книге.
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Book.

        Returns:
            Строка в формате: "Книга "название_книги""
        """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта Book, которое можно использовать для создания нового объекта.

        Returns:
            Строка в формате: "Book(id_={self.id}, name='{self.name}', pages={self.pages})"
        """
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


# TODO написать класс Library

class Library:
    """
    Класс, представляющий библиотеку с книгами.
    """

    def __init__(self, books=None):
        """
        Инициализирует библиотеку списком книг.

        Args:
            books (list, optional): Список книг для инициализации библиотеки.
                Если не указан, создается пустой список.
        """
        self.books = books if books is not None else []

    def get_next_book_id(self):
        """
        Возвращает идентификатор для добавления новой книги.
        """
        if not self.books:
            return 1
        else:
            return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id):
        """
        Возвращает индекс книги по её идентификатору.

        Args:
            book_id (int): Идентификатор книги для поиска.

        Returns:
            int: Индекс книги в списке.

        Raises:
            ValueError: Если книга с указанным id не найдена.
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
