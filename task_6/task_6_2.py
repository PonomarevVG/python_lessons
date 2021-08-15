# Задание 6.2
# Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
#
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:
    def __init__(self, n_length, n_width):
        self._length = n_length
        self._width = n_width

    def mass_calc(self, thickness, weight_per_unit):
        print(f'Требуемая масса асфальта = {self._width} м*{self._length} м*{weight_per_unit} кг*{thickness} см = '
              f'{int(self._width * self._length * weight_per_unit * thickness / 10000)} т.')


current_road = Road(5000, 20)
current_road.mass_calc(5, 25)