if __name__ == "__main__":
    # Write your solution here
    pass

import doctest


class Animal:
    """Базовый класс для всех животных."""

    def __init__(self, type: str, name: str, age: int) -> None:
        """Конструктор класса Животное."""
        self.type = type
        self.name = name
        self.age = age

    def __str__(self) -> str:
        """Возвращает строковое представление животного."""
        return f"{self.type} по имени {self.name}, возраст: {self.age}"

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта для отладки."""
        return f"Животное('{self.type}', '{self.name}', {self.age})"

    def make_sound(self) -> str:
        """Общий метод для издания звука."""
        return "Звук животного"

    def get_info(self) -> str:
        """Возвращает информацию о животном."""
        return f"Это {self.type}."


class Cat(Animal):
    """Дочерний класс для кошек."""

    def __init__(self, name: str, age: int, breed: str) -> None:
        """Конструктор класса Кошка, расширяет конструктор базового класса."""
        super().__init__("Кошка", name, age)
        self.breed = breed

    def __str__(self) -> str:
        """Перегружает строковое представление кошки."""
        return f"{self.breed} по имени {self.name}, возраст: {self.age}"

    def make_sound(self) -> str:
        """Перегружает метод издания звука для кошек."""
        return "Мяу!"

    def get_info(self) -> str:
        """Перегружает информацию о животном."""
        return f"Это кошка породы {self.breed}."




class Transport:
    """Базовый класс для всех видов транспорта."""

    def __init__(self, type: str, name: str, function: str) -> None:
        """Конструктор класса Транспорт."""
        self.type = type
        self.name = name
        self.function = function

    def __str__(self) -> str:
        """Возвращает строковое представление транспорта."""
        return f"{self.type} по названию {self.name}, функции: {self.function}"

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта для отладки."""
        return f"Транспорт('{self.type}', '{self.name}', {self.function})"

    def defind_function(self) -> str:
        """Общий метод для определения функции транспорта."""
        return "Функция транспорта"

    def get_info(self) -> str:
        """Возвращает информацию о транспорте."""
        return f"Это {self.type}."


class Passenger_Car(Transport):
    """Дочерний класс для транспорта."""

    def __init__(self, name: str, function: str, country: str, brand: str) -> None:
        """Конструктор класса Легковые автомобил, расширяет конструктор базового класса."""
        super().__init__("Легковые автомобили", name, function)
        self.country = country
        self.brand = brand

    def __str__(self) -> str:
        """Перегружает строковое представление легковых автомобилей."""
        return f"{self.country} по названию {self.name}, функция: {self.function}"

    def defind_function(self) -> str:
        """Перегружает метод определения функции для легковых автомобилей."""
        return "Перевозка пассажиров"

    def get_info(self) -> str:
        """Перегружает информацию о легковом автомобиле."""
        return f"Это легковой автомобиль марки {self.brand} из {self.country}."


class Germany_passenger_car(Passenger_Car):
    """Дочерний класс для легковых автомобилей."""

    def __init__(self, country: str, brand: str, car_model = str, release_year = int, configuration = str) -> None:
        """Конструктор класса Немецкие легковые автомобили, расширяет конструктор дочернего класса легковых автомобилей."""
        super().__init__("Немецкие легковые автомобили", country, brand)
        self.brand = brand
        self.model = car_model
        self.year = release_year
        self.configuration = configuration

    def __str__(self) -> str:
        """Перегружает строковое представление немецких легковых автомобилей."""
        return f"{self.brand} по модели {self.model}, год выпуска: {self.year}, комплектации: {self.configuration}"

    def available_configurations(self) -> str:
        """Перегружает метод вывода имеющихся комплектаций автомобиля."""
        return "Автомобили есть в базовой, комфорт и премиум комплектациях."

    def get_info(self) -> str:
        """Перегружает информацию о животном."""
        return f"Это {self.brand} {self.model} {self.year} года выпуска в {self.configuration} комплектации."


if __name__ == "__main__":
    doctest.testmod()
