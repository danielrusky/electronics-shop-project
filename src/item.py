import csv

import pytest

class InstantiateCSVError(Exception):
    def __init__(self, message=" Файл item.csv поврежден "):
        super().__init__(message)
        
class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 0.8
    all = []

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
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них')
        return self.quantity + other.quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) > 10:
            self.__name = new_name[:10]
        else:
            self.__name = new_name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate


    @classmethod
    def instantiate_from_csv(cls, csv_file="../src/items.csv"):
        try:
            with open(csv_file, 'r', encoding='windows-1251') as file:
                
                reading_csv = csv.DictReader(file, delimiter=',')
                for i in reading_csv:
                    next(reading_csv)
                    if len(i) != 3:
                        raise InstantiateCSVError
                    name = str(i['name'])
                    price = float(i['price'])
                    quantity = int(i['quantity'])
                    cls(name, price, quantity)
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")
        
            
            

    @staticmethod
    def string_to_number(string):
        string = int(float(string))
        return string
###
