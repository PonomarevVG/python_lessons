# Задание 8.6
# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

from abc import ABC, abstractmethod


class OfficeEq(ABC):
    name = None

    def __init__(self, n_number):
        if not n_number:
            self.print_title()
        self._number = n_number if n_number else input('Введите инвентарный номер устройства: ')

    @abstractmethod
    def __str__(self):
        pass

    @classmethod
    def print_title(cls):
        print(f'Введите значения характиристик нового устройства типа {cls.name}')

    @staticmethod
    def get_eq_types_name(eq_list):
        name_set = set()
        for eq in eq_list:
            name_set.add(eq.name)
        return name_set


class Printer(OfficeEq):
    name = 'Принтер'

    def __init__(self, n_number=None, n_cartridge_model=None):
        super().__init__(n_number)
        self._cartridge_model = n_cartridge_model if n_cartridge_model else input('Введите модель картриджа, используемую принтером: ')

    def __str__(self):
        return 'Принтер с инвентарным номером {}, модель картриджа {}'.format(self._number, self._cartridge_model)


class Scanner(OfficeEq):
    name = 'Сканер'

    def __init__(self, n_number=None, n_pages_per_second=None):
        super().__init__(n_number)
        if n_pages_per_second:
            self._pages_per_second = n_pages_per_second
        else:
            self._pages_per_second = input('Введите число страниц, сканируемых в секунду: ')
            if not self._pages_per_second.isdigit():
                self._pages_per_second = 0

    def __str__(self):
        return 'Сканер с инвентарным номером {}, сканирует {} страниц в секунду'.format(self._number, self._pages_per_second)


class Xerox(OfficeEq):
    name = 'Ксерокс'

    def __init__(self, n_number=None, n_pages_per_minute=None):
        super().__init__(n_number)
        self._pages_per_minute = n_pages_per_minute
        if n_pages_per_minute:
            self._pages_per_minute = n_pages_per_minute
        else:
            self._pages_per_minute = input('Введите число страниц, ксерокопируемых в минуту: ')
            if not self._pages_per_minute.isdigit():
                self._pages_per_minute = 0

    def __str__(self):
        return 'Ксерокс с инвентарным номером {}, копирует {} страниц в минуту'.format(self._number, self._pages_per_minute)


class Warehouse:
    warehouses_count = 0

    def __init__(self):
        self._office_eqs = []
        Warehouse.warehouses_count += 1
        self.warehouses_number = Warehouse.warehouses_count

    def __del__(self):
        Warehouse.warehouses_count -= 1

    def get(self, eq_list):
        for eq in eq_list:
            self._office_eqs.append(eq)

    def show_technics(self):
        print(f'Техника на складе № {self.warehouses_number}:')
        for eq in self._office_eqs:
            print(eq)
        print('')

    @staticmethod
    def validate_num(num):
        return int(num) if num.isdigit() and int(num) > 0 else None

    def send_to_company(self, company, eq_type, amount, department):
        current_eqs = []

        print(f'Отправка со склада № {self.warehouses_number}:')
        for eq in self._office_eqs:
            if type(eq).name == eq_type:
                print(f'{eq} отправлен в департамент {department}')
                current_eqs.append(eq)
                self._office_eqs.remove(eq)
                amount -= 1
                if amount == 0:
                    break
        company.get(current_eqs, department)
        if len(current_eqs) == 0:
            print('Ничего не отправлено')
        print('')


class Company:
    def __init__(self):
        self._office_eqs = dict()

    def get(self, eq_list, department='Дирекция'):
        for eq in eq_list:
            if type(eq).name in self._office_eqs:
                self._office_eqs[type(eq).name].append({'eq': eq, 'department': department})
            else:
                self._office_eqs[type(eq).name] = [{'eq': eq, 'department': department}]

    def show_technics(self):
        print('Техника в департаментах компании:')
        for name, eq_group in self._office_eqs.items():
            print(f'Орг. техника. Вид: {name}. Количество единиц: {len(eq_group)}')
            for eq in eq_group:
                print(f"Единица техники {eq['eq']} находится в департаменте: {eq['department']}")
        print('')

# Устройства могут инициалировться как в параметрах конструктора, так и с клавиатуры, если параметр = None
office_eq = [Printer(), Scanner('6567888', 3), Printer('4564889', 'X6347AB'), Xerox('6567888', 5)]

current_warehouse = Warehouse()
current_company = Company()
current_warehouse.get(office_eq)
current_warehouse.show_technics()

eq_types_names = OfficeEq.get_eq_types_name(office_eq)
print(f"Существующие типы устройств: {' '.join(map(str,eq_types_names))}")

current_eq_type = input('Введите тип устройства для отправки на склад: ')
while not (current_eq_type in eq_types_names):
    print('Тип устройства не входит в перечень существующих устройств!')
    current_eq_type = input('Введите тип устройства для отправки на склад: ')

current_eq_count = Warehouse.validate_num(input('Введите количество устройств для отправки на склад: '))
while not current_eq_count:
    print('Число устройств для отправки должно быть натуральным числом!')
    current_eq_count = Warehouse.validate_num(input('Введите количество устройств для отправки на склад: '))

current_warehouse.send_to_company(current_company, current_eq_type, current_eq_count, input('Введите название департамента для отправки устройства: '))

current_company.show_technics()
current_warehouse.show_technics()
