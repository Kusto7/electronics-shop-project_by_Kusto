import csv

from src.settings import DATA_PATH


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.total_price = 0
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        self.total_price = self.price * self.quantity
        return self.total_price

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate
        return self.price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name: str):
        if len(new_name) > 10:
            raise ValueError("Длина наименования товара превышает 10 символов.")
        else:
            self.__name = new_name

    @classmethod
    def instantiate_from_csv(cls):
        with open(DATA_PATH, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            Item.all.clear()
            for item in reader:
                cls(item['name'], item['price'], item['quantity'])

    @staticmethod
    def string_to_number(number):
        if '.' in number:
            int_number, false_number = number.split('.')
            return int(int_number)
        else:
            return int(number)
