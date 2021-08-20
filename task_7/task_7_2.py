# Задание 7.2
# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
# одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Wear(ABC):
    @abstractmethod
    def __init__(self, param):
        pass

    @abstractmethod
    def fabric_amount_needed(self):
        pass


class Suit(Wear):
    def __init__(self, param):
        self.h = param

    @property
    def fabric_amount_needed(self):
        return 2 * self.h + 0.3


class Coat(Wear):
    def __init__(self, param):
        self.v = param

    @property
    def fabric_amount_needed(self):
        return self.v / 6.5 + 0.5


current_coat = Coat(42)
print(f'Расход ткани на пальто размера {current_coat.v} = {current_coat.fabric_amount_needed}')

current_suit = Suit(1.8)
print(f'Расход ткани на костюм для человека ростом {current_suit.h} м = {current_suit.fabric_amount_needed}')