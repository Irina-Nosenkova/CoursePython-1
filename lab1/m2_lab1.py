# TODO Написать 3 класса с документацией и аннотацией типов

import doctest


class Fuel_tank:
    def __init__(self, capacity_volume: float, occupied_volume: float):
        """
        Создание и подготовка к работе объекта "Топливный бак"

        :param capacity_volume: Объем топливного бака
        :param occupied_volume: Объем залитого топлива

        Примеры:
        >>> fueltank = Fuel_tank(50, 0)  # инициализация экземпляра класса
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем топливного бака должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем топливного бака должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Количество топлива должно быть int или float")
        if occupied_volume < 0:
            raise ValueError("Количество топлива не может быть отрицательным числом")
        self.occupied_volume = occupied_volume

    def is_empty_fueltank(self) -> bool:
        """
        Функция которая проверяет является ли топливный бак пустым

        :return: Является ли топливный бак пустым

        Примеры:
        >>> fueltank = Fuel_tank(50, 0)
        >>> fueltank.is_empty_fueltank()
        """
        ...

    def add_petrol_to_fueltank(self, petrol: float) -> None:
        """
        Добавление бензина в топливный бак.
        :param petrol: Объем добавляемого бензина

        :raise ValueError: Если количество добавляемого бензина превышает свободное место в топливном баке, то вызываем ошибку

        Примеры:
        >>> fueltank = Fuel_tank(50, 0)
        >>> fueltank.add_petrol_to_fueltank(34)
        """
        if not isinstance(petrol, (int, float)):
            raise TypeError("Количество добавляемого бензина должно быть типа int или float")
        if petrol < 0:
            raise ValueError("Количество добавляемого бензина должно быть положительным числом")
        ...

    def remove_petrol_from_fueltank(self, estimate_petrol: float) -> None:
        """
        Извлечение бензина из топливного бака.

        :param estimate_petrol: Объем извлекаемого бензина
        :raise ValueError: Если количество извлекаемого бензина превышает количество бензина в топливном баке,
        то возвращается ошибка.

        :return: Объем реально извлеченного бензина

        Примеры:
        >>> fueltank = Fuel_tank(50, 47)
        >>> fueltank.remove_petrol_from_fueltank(13)
        """
        ...



class Flowers_for_sale:
    """
   Класс цветов для продажи.
    """
    def __init__(self, name: str, durability: int, price: float):
        if not isinstance(name, str):
            raise TypeError("Название должно быть строкой")
        if not isinstance(price, (int, float)):
            raise TypeError("Цена должна быть числом")
        if price < 0:
            raise ValueError("Цена должна быть неотрицательным числом")
        self.name = name
        self.durability = durability
        self.price = price

    def average_durability(self, average_durability: float) -> float:
        """Вычисляет среднюю продолжительность стойкости цветов в вазе"""

    def calculate_discount(self, discount_percentage: float) -> float:
        """
        Вычисляет цену со скидкой.
        """
        pass



class SocialNetwork:
    """
    Класс, представляющий социальную сеть.
    """
    def __init__(self, name: str, user_count: int):
        if not isinstance(user_count, int):
            raise TypeError("Количество пользователей должно быть целым числом")
        self.name = name
        self.user_count = user_count

    def subscriptions(self, user_id: int, user_subscriptions: int) -> int:
        """Выводит количество подписчиков у пользователя"""

    def post_message(self, user_id: int, message: str) -> bool:
        """Публикует сообщение от пользователя."""
        pass


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
