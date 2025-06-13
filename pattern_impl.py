from abc import ABC, abstractmethod

class Renovation(ABC):
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass

class BaseRenovation(Renovation):
    def get_description(self):
        return "Базовый ремонт: окраска стен"

    def get_cost(self):
        return 100000  # Примерная базовая стоимость

class RenovationDecorator(Renovation):
    def __init__(self, renovation: Renovation):
        self._renovation = renovation

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass

class LaminateFloorDecorator(RenovationDecorator):
    def get_description(self):
        return self._renovation.get_description() + ", ламинат на полу"

    def get_cost(self):
        return self._renovation.get_cost() + 30000

class StretchCeilingDecorator(RenovationDecorator):
    def get_description(self):
        return self._renovation.get_description() + ", натяжной потолок"

    def get_cost(self):
        return self._renovation.get_cost() + 40000

class BathTileDecorator(RenovationDecorator):
    def get_description(self):
        return self._renovation.get_description() + ", плитка в ванной"

    def get_cost(self):
        return self._renovation.get_cost() + 25000

# Пример использования:
if __name__ == '__main__':
    renovation = BaseRenovation()
    renovation = LaminateFloorDecorator(renovation)
    renovation = StretchCeilingDecorator(renovation)
    print(renovation.get_description())
    print("Цена:", renovation.get_cost())
