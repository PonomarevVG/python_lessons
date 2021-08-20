# Задание 6.5
# Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationary:

    def __init__(self, n_title):
        self.title = n_title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationary):

    def __init__(self, n_title):
        super().__init__(n_title)

    def draw(self):
        print(f'Запуск отрисовки ручкой. Название: {self.title}')


class Pencil(Stationary):

    def __init__(self, n_title):
        super().__init__(n_title)

    def draw(self):
        print(f'Запуск отрисовки карандашом. Название: {self.title}')


class Handle(Stationary):

    def __init__(self, n_title):
        super().__init__(n_title)

    def draw(self):
        print(f'Запуск отрисовки маркером. Название: {self.title}')


current_stationary = Stationary('Канцелярская приндлежность')
current_stationary.draw()

current_pen = Pen('Ручка')
current_pen.draw()

current_pencil = Pencil('Карандаш')
current_pencil.draw()

current_handle = Handle('Маркер')
current_handle.draw()
