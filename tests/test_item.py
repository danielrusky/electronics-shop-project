"""Здесь надо написать тесты с использованием pytest для модуля item."""  #
from src.item import Item


def test_calculate_total_prices():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    item1.calculate_total_price()
    assert item1.price * item1.quantity == 200000
    assert item2.price * item2.quantity == 100000

    # устанавливаем новый уровень цен

    # применяем скидку


def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    item1.apply_discount()

    assert item1.price == 8000.0
    assert item2.price == 20000.0


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    assert item1.__repr__() == Item("Смартфон", 10000, 20)
    assert item2.__repr__() == Item("Ноутбук", 20000, 5)


def test_str():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    assert item1.__str__() == "Сматрфон"
    assert item2.__str__() == "Ноутбук"


def test_add():
    assert Item.
##
