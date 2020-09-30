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
    def __init__(self, speed, color, name, is_police: bool = False):
        self.speed = speed
        self.color = color
        self.name = name + ' (POLICE)' if is_police else name

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn(self, direction):
        return f'{self.name} повернула {direction}'

    def show_speed(self):
        return f'Скорость {self.name} - {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 60:
            return f"Вы превысили скорость!, {super().show_speed()}"
        else:
            return f"{super().show_speed()} - Скорость разрешенная"


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 40:
            return f"Вы превысили скорость!, {super().show_speed()}"
        else:
            return f"{super().show_speed()} - Скорость разрешенная"


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


mazda_car = TownCar(50, 'Металлик', 'Mazda')
gaz_car = WorkCar(60, 'Белый', 'Газель')
ferrari_car = SportCar(210, 'Красный', 'Ferrari')
vaz_car = PoliceCar(100, 'Беж', 'ВАЗ-2114')
print(f'Автомобиль {mazda_car.turn("налево")}. {mazda_car.show_speed()}')
print(gaz_car.show_speed())
print(mazda_car.show_speed())
print(ferrari_car.show_speed(), ferrari_car.name, ferrari_car.color)
print(vaz_car.show_speed())
