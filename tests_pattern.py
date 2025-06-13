import pytest
from unittest.mock import patch

from ccc import (
    BaseRenovation, LaminateFloorDecorator,
    StretchCeilingDecorator, BathTileDecorator
)


def test_base_renovation():
    renovation = BaseRenovation()
    assert renovation.get_description() == "Базовый ремонт: окраска стен"
    assert renovation.get_cost() == 100000


def test_laminate_decorator():
    renovation = LaminateFloorDecorator(BaseRenovation())
    assert "ламинат" in renovation.get_description()
    assert renovation.get_cost() == 130000


def test_multiple_decorators():
    renovation = BaseRenovation()
    renovation = LaminateFloorDecorator(renovation)
    renovation = StretchCeilingDecorator(renovation)
    renovation = BathTileDecorator(renovation)
    desc = renovation.get_description()
    assert all(word in desc for word in ["ламинат", "натяжной потолок", "плитка"])
    assert renovation.get_cost() == 100000 + 30000 + 40000 + 25000


def test_invalid_usage():  # тест с негатив сцен
    with pytest.raises(TypeError):
        # BathTileDecorator требует объект Renovation, а не строку
        BathTileDecorator("not a renovation")


def test_laminate_decorator_cost_mock():
    renovation = BaseRenovation()
    decorator = LaminateFloorDecorator(renovation)
    with patch.object(BaseRenovation, 'get_cost', return_value=50000):
        assert decorator.get_cost() == 50000 + 30000  # замокали базовый кост
