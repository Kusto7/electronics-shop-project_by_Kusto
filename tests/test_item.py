"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item
from src.phone import Phone


@pytest.fixture
def my_object():
    item1 = Item('Смартфон', 10000, 20)
    return item1


def test_calculate(my_object):
    my_object.calculate_total_price()
    assert my_object.calculate_total_price() == 200000


def test_pay_rate(my_object):
    Item.pay_rate = 0.8
    my_object.apply_discount()
    assert my_object.price == 8000


def test_create_object(my_object):
    Item.pay_rate = 1.0
    assert my_object.price == 10000
    assert my_object.name == 'Смартфон'
    assert my_object.quantity == 20
    assert my_object.total_price == 0
    assert len(Item.all) != 0
    assert Item.pay_rate == 1.0


def test_name(my_object):
    my_object.name = 'Телефон'
    assert my_object.name == 'Телефон'


def test_value_error_name(my_object):
    with pytest.raises(ValueError):
        my_object.name = 'Телефонфонфон'


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'


def test_test_instantiate_from_csv_file_found(capsys):
    Item.file_csv_cls_path = "items.csv"
    Item.instantiate_from_csv()
    captured = capsys.readouterr()
    assert captured.out == "Отсутствует файл item.csv\n"


def test_item_corrupted(capsys):
    Item.file_csv_cls_path = '../homework-2/items_corrupted.csv'
    Item.instantiate_from_csv()
    captured = capsys.readouterr()
    assert captured.out == "Файл item.csv поврежден\n"


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr_str_item():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert str(item1) == 'Смартфон'


def test_add_class():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
    with pytest.raises(Exception):
        phone1 + 5
