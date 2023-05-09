import pytest

from src.keyboard import Keyboard


@pytest.fixture
def my_object():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    return kb


def test_name_keyboard(my_object):
    assert str(my_object) == "Dark Project KD87A"


def test_language(my_object):
    assert str(my_object.language) == "EN"

    my_object.change_lang()
    assert str(my_object.language) == "RU"
    my_object.change_lang().change_lang()
    assert str(my_object.language) == "RU"


def test_value_error_name(my_object):
    with pytest.raises(AttributeError):
        my_object.language = 'CH'
