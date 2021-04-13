class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} начел движение.'

    def stop(self):
        return f'{self.name} остановился.'

    def turn_right(self):
        return f'{self.name} повернул на право'

    def turn_left(self):
        return f'{self.name} повернул влево'

    def show_speed(self):
        return f'Текущая скорость {self.name} - {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость городского автомобиля {self.name} - {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} выше разрешенного для городского автомобиля'
        else:
            return f'Скорость {self.name} нормальна для городской машины'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость рабочей машины {self.name} - {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} выше разрешенного, для рабочей машины'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} из отдела полиции.'
        else:
            return f'{self.name} не из отдела полиции.'


Forester = SportCar(100, 'Синий', 'Forester', False)
Crown = TownCar(30, 'Чёрный', 'Crown', False)
Solaris = WorkCar(70, 'Белый', 'Solaris', True)
Mark2 = PoliceCar(110, 'Серый', 'Mark2', True)
print(Solaris.turn_left())
print(f'Когда {Crown.turn_right()}, тогда {Forester.stop()}')
print(f'{Solaris.show_speed()}')
print(f'{Solaris.name} - {Solaris.color}')
print(f'{Forester.name} полицейская машина? {Forester.is_police}')
print(f'{Solaris.name}  полицейская машина? {Solaris.is_police}')
print(Forester.show_speed())
print(Crown.show_speed())
print(Mark2.police())
print(Mark2.show_speed())
