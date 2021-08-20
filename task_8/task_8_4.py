# Задание 8.4
# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

from abc import ABC, abstractmethod


class OfficeEq(ABC):
    def __init__(self, n_number):
        self._number = n_number

    @abstractmethod
    def __str__(self):
        pass


class Printer(OfficeEq):
    def __init__(self, n_number, n_cartridge_model):
        super().__init__(n_number)
        self._cartridge_model = n_cartridge_model

    def __str__(self):
        return 'Принтер с инвентарным номером {}, модель картриджа {}'.format(self._number, self._cartridge_model)


class Scanner(OfficeEq):
    def __init__(self, n_number, n_pages_per_second):
        super().__init__(n_number)
        self._pages_per_second = n_pages_per_second

    def __str__(self):
        return 'Сканер с инвентарным номером {}, сканирует {} страниц в секунду'.format(self._number, self._pages_per_second)


class Xerox(OfficeEq):
    def __init__(self, n_number, n_pages_per_minute):
        super().__init__(n_number)
        self._pages_per_minute = n_pages_per_minute

    def __str__(self):
        return 'Ксерокс с инвентарным номером {}, копирует {} страниц в минуту'.format(self._number, self._pages_per_minute)


class Warehouse:
    supplies_count = 0

    def __init__(self, *args):
        self.office_eqs = args
        Warehouse.supplies_count += 1
        print('Открылся новый склад!')

    def __del__(self):
        Warehouse.supplies_count -= 1


office_eq = [Printer('3674889', 'X6737AB'), Scanner('6567888', 3), Xerox('6567888', 5)]
for eq in office_eq:
    print(eq)

current_warehouse = Warehouse()

