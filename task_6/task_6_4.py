# Задание 6.4
# Реализуйте базовый класс Car.
#
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда); опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:
    def __init__(self, n_speed, n_color, n_name, n_is_police):
        self.speed = n_speed
        self.color = n_color
        self.name = n_name
        self.is_police = n_is_police

    def go(self):
        print(f'{self.name}: Машина поехала')

    def stop(self):
        print(f'{self.name}: Машина остановилась')

    def turn(self, direction):
        print(f'{self.name}: Машина повернула {direction}')

    def show_speed(self):
        print(f'{self.name}: Скорость автомобиля равна = {self.speed} км/ч')

class PoliceCar(Car):
    def __init__(self, n_speed, n_color, n_name):
        super().__init__(n_speed, n_color, n_name, True)


class TownCar(Car):
    def __init__(self, n_speed, n_color, n_name):
        super().__init__(n_speed, n_color, n_name, False)

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'{self.name}: Превышение скорости')


class WorkCar(Car):
    def __init__(self, n_speed, n_color, n_name):
        super().__init__(n_speed, n_color, n_name, False)

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f'{self.name}: Превышение скорости')


current_car = Car(70, 'red', 'Tayota Corolla', False)
current_car.go()
current_car.stop()
current_car.turn('вправо')
current_car.show_speed()

police_car = PoliceCar(80, 'white', 'Mazda RX5')
police_car.show_speed()

town_car = TownCar(70, 'blue', 'Henday Solaris')
town_car.show_speed()

work_car = WorkCar(50, 'yellow', 'Ford Harley')
work_car.show_speed()
