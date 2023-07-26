"""Здесь надо написать тесты с использованием pytest для модуля item."""  #
import pytest

from src.item import Item
from src.keyboard import Keyboard


@pytest.fixture
def example():
    Item.pay_rate = 0.8
    return Item("Смартфон", 10000, 20)


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


def test_repr(example):
    assert example.__repr__() == "Item('Смартфон', 10000, 20)"


def test_str(example):
    assert example.__str__() == "Смартфон"


def test_add(example):
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    assert item1 + item2 == 25


def test_keyboard():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"
    assert str(kb.language) == "EN"
    assert kb.name == 'Dark Project KD87A'
    assert kb.price == 9600
    assert kb.quantity == 5


###
