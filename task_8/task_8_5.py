# Задание 8.5
# Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и передачу
# в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру (например, словарь).

from abc import ABC, abstractmethod


class OfficeEq(ABC):
    def __init__(self, n_number):
        self._number = n_number

    @abstractmethod
    def __str__(self):
        pass


class Printer(OfficeEq):
    name = 'Принтер'

    def __init__(self, n_number, n_cartridge_model):
        super().__init__(n_number)
        self._cartridge_model = n_cartridge_model

    def __str__(self):
        return 'Принтер с инвентарным номером {}, модель картриджа {}'.format(self._number, self._cartridge_model)


class Scanner(OfficeEq):
    name = 'Сканер'

    def __init__(self, n_number, n_pages_per_second):
        super().__init__(n_number)
        self._pages_per_second = n_pages_per_second

    def __str__(self):
        return 'Сканер с инвентарным номером {}, сканирует {} страниц в секунду'.format(self._number, self._pages_per_second)


class Xerox(OfficeEq):
    name = 'Ксерокс'

    def __init__(self, n_number, n_pages_per_minute):
        super().__init__(n_number)
        self._pages_per_minute = n_pages_per_minute

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

    def send_to_company(self, company, eq_type, amount, department):
        if amount <= 0:
            return
        current_eqs = []

        print(f'Отправка со склада № {self.warehouses_number}:')
        for eq in self._office_eqs:
            if type(eq).name == eq_type:
                print(f'{eq} отправлен в демартамент {department}')
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
                print(f"Единица техники {eq['eq']} находится в демартаменте: {eq['department']}")
        print('')


office_eq = [Printer('3674889', 'X6737AB'), Scanner('6567888', 3), Printer('4564889', 'X6347AB'), Xerox('6567888', 5)]

current_warehouse = Warehouse()
current_company = Company()
current_warehouse.get(office_eq)
current_warehouse.show_technics()
current_warehouse.send_to_company(current_company, 'Принтер', 2, 'Бухгалтерия')
current_company.show_technics()
current_warehouse.show_technics()

