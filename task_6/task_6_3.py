# Задание 6.3
# Реализовать базовый класс Worker (работник).
#
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
# дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров.

class Worker:

    def __init__(self, n_name, n_surname, n_position, n_wage, n_bonus):
        self.name = n_name
        self.surname = n_surname
        self.position = n_position
        self._income = {"wage": n_wage, "bonus": n_bonus}


class Position(Worker):

    def __init__(self, n_name, n_surname, n_position, n_wage, n_bonus):
        super().__init__(n_name, n_surname, n_position, n_wage, n_bonus)

    def get_full_name(self):
        print(f'Полное имя сотрудника {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Полный доход с учетом премии = {self._income["wage"] + self._income["bonus"]}')


first_worker = Position('Иван', 'Иванов', 'Разнорабочий', 10000, 1000)
first_worker.get_full_name()
first_worker.get_total_income()

second_worker = Position('Петр', 'Петров', 'Начальник отдела', 20000, 2000)
second_worker.get_full_name()
second_worker.get_total_income()
