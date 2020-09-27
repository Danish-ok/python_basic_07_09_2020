"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также
покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn(self, direction):
        return f'{self.name} повернула {direction}'

    def show_speed(self):
        return f'Скорость {self.name} - {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return "Вы превысили скорость!"
        else:
            return "Скорость разрешенная"


class SportCar(Car):
    def sport_car(self):
        pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return "Вы превысили скорость!"
        else:
            return "Скорость разрешенная"


class PoliceCar(Car):
    def police_car(self):
        if self.police_car():
            return 'Это полицейская машина'
        else:
            return 'Это не полицейская машина'


mazda_car = TownCar(50, 'Металлик', 'Mazda', False)
gaz_car = WorkCar(60, 'Белый', 'Газель', True)
ferrari_car = SportCar(210, 'Красный', 'Ferrari', False)
vaz_car = PoliceCar(100, 'Беж', 'ВАЗ-2114', True)
print(f'Автомобиль {mazda_car.turn("налево")} со скоростью -  {mazda_car.show_speed()}')
print(gaz_car.show_speed())
print(mazda_car.show_speed())
print(ferrari_car.show_speed(), ferrari_car.name, ferrari_car.color)
