import csv

from src.InstantiateCSVError import InstantiateCSVError
from src.settings import DATA_PATH


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    file_csv_cls_path = DATA_PATH

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
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
        try:
            with open(Item.file_csv_cls_path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                Item.all.clear()
                correct_colons = ['name', 'price', 'quantity']
                if reader.fieldnames == correct_colons:
                    for item in reader:
                        cls(item['name'], item['price'], item['quantity'])
                else:
                    raise InstantiateCSVError
        except InstantiateCSVError:
            print('Файл item.csv поврежден')

        except FileNotFoundError:
            print("Отсутствует файл item.csv")

    @staticmethod
    def string_to_number(number):
        if '.' in number:
            int_number, false_number = number.split('.')
            return int(int_number)
        else:
            return int(number)

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        else:
            print("Объект не является классом")
            raise Exception
